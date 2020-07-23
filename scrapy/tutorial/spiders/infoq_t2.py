# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import json
import datetime
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from string import Template
from dateutil import parser

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random
import numpy
import pandas as pd
from elasticsearch import Elasticsearch
import logging


env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))


class AliSpider(scrapy.Spider):
    # 593
    name = "infoq_t2"

    mainUrl = "https://www.infoq.cn/public/v1/article/getList"

    page = 0
    pageSize = 20
    last_score = 0
    source = "infoq"
    ids = [
        1,8,3,36,48,4,31,6,11,17,7,15,9,157,26,13,
        147,33,14,21,38,43,29,107,32,1122,10,12,41,
        61,30,19,34,69,20,25,16,106,81,18,68,65,51,
        24,70,108,84,146,45,1118,54,23,145,22,79,78,
        64,96,50,42,57,74,28,1121,37,27,159,44,40,56,
        52,35,53,39,126,55,47,46,127,119,98,82,67,66,
        88,59,63,58,129,1131,62,116,77,1128,125,89,
        71,87,60,49,118,76,1117,80,1127,1134,1120,72,
        73,152,75,141,139,85,148,117,138,137,91,144,
        133,132,1123,86,111,94,1137,90,1111,142,154,
        134,1115,92,1124,113,1135,121,97,1113,95,122,
        112,135,93,140,158,143,128,1133,130,114,120,
        110,160,150,131,123,1112,1132,149,1126,151,136,
        115,155,153,1116,1129,1119,1139,1125,1114,124,
        1130,1138   
    ]
    
    topic_list = []

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "www.infoq.cn",
        "Origin": "https://www.infoq.cn",
        "Pragma": "no-cache",
        "Referer": "https://www.infoq.cn/topics",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 ,Safari/537.36"
    }

    def get_body(self,id=1,score=0):
        formdata =  {
            "id":id,
            "size": 50,
            "type":0
        }

        if score != 0 :
            formdata['score'] = int(score)
        return json.dumps(formdata)

    def start_requests(self):
        last = {
            "id":self.ids.pop(0),
            "score":0
        }

        yield scrapy.FormRequest(url=self.mainUrl,body=self.get_body(id = last['id']), method="POST",headers=self.headers, callback=lambda response, last=last: self.parse(response, last))

    def parse(self, response, last):
        resp = json.loads(response.text)

        logging.info("_id: "+str(last['id']))
        logging.info("score: "+str(last['score']))


        if len(resp['data']) == 0:
            if len(self.ids)>0:
                new_last = {
                    "id":self.ids.pop(0),
                    "score":0
                }
                yield scrapy.FormRequest(url=self.mainUrl,body=self.get_body(id = new_last['id']), method="POST",headers=self.headers, callback=lambda response, last=new_last: self.parse(response, last))
            else:
                print("spider end 1")
                os._exit(0)
        else:
            bulk = []
            for item in resp['data']:

                doc = {}
                doc['title'] = item['article_title']
                doc['url'] = "https://www.infoq.cn/article/"+item['uuid']
                doc['summary'] = item['article_summary']

                doc['created_at'] = datetime.datetime.fromtimestamp(
                    int(item['ctime'])/1000,None)

                doc['created_year'] = doc['created_at'].strftime("%Y")

                if 'author' in item:
                    doc['author'] = item['author'][0]['nickname']

                if 'topic' in item:
                    doc['tag'] = list(map(lambda x: x['alias'],item['topic']))

                doc['source'] = self.source
                doc['source_id'] = item['aid']
                doc['source_score'] = 0

                bulk.append(
                    {"index": {"_index": "article"}})
                resp2 = bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="article", body=bulk)

            last_score = resp['data'][-1]['score']
            
            if last['score'] == last_score:
                if len(self.ids)>0:
                    new_last = {
                        "id":self.ids.pop(0),
                        "score":0
                    }
                    yield scrapy.FormRequest(url=self.mainUrl,body=self.get_body(id = new_last['id']), method="POST",headers=self.headers, callback=lambda response, last=new_last: self.parse(response, last))
                else:
                    print("spider end 2")
                    os._exit(0)

            last['score'] =  last_score
            
            yield scrapy.FormRequest(url=self.mainUrl,body=self.get_body(score=last_score,id=last['id']), method="POST",headers=self.headers, callback=lambda response, last=last: self.parse(response, last))
