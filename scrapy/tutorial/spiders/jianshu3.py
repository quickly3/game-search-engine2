# -*- coding:UTF-8 -*-
#


import scrapy
import sys
import sqlalchemy
import os
import json
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import time, datetime

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random
from string import Template

from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)

class AliSpider(scrapy.Spider):
    # 593
    name = "jianshu3"

    domain = 'https://www.jianshu.com'
    url_list = []
    slug_end = True
    current = 0
    handle_httpstatus_list = [404]
    scroll_id = None

    def __init__(self):

        self.url_model = Template(
            "https://www.jianshu.com/c/${slug}?order_by=top&page=${page}")

        self.headers1 = {
            "Accept": "text/html, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
            "x-infinitescroll": "true",
            "x-requested-with": "XMLHttpRequest"
        }

    def getCount(self):
        body = {
            "query":{
                "query_string": {
                    "query": "source:jianshu && -created_at:*"
                }
            }
        }
        resp = es.count(index="article",body=body)
        self.count = resp['count']

    def getSlugUrl(self):
        self.current+=1

        if self.scroll_id == None:
            body = {
                "query":{
                    "query_string": {
                        "query": "source:jianshu && -created_at:*"
                    }
                }
            }
            query = es.search(index="article",body=body,size=1,scroll="1m")
            self.scroll_id = query['_scroll_id']
        else:

            query = es.scroll(scroll_id=self.scroll_id,scroll="1m")
            self.scroll_id = query['_scroll_id']            

        hits = query['hits']['hits']
        if len(hits) >0 :
            return {
                "url":hits[0]['_source']['url'],
                "id":hits[0]['_id']
            }
        else:
            return False

    def start_requests(self):
        self.getCount()
        data = self.getSlugUrl()
        print(str(self.current)+"/"+str(self.count));
        yield scrapy.Request(url=data['url'], headers=self.headers1, callback=lambda response, id=data['id']: self.parse(response, id))

    def parse(self, response, id):

        if response.status == 400:
            resp = response.xpath('//*[@id="__NEXT_DATA__"]/text()').get()
            resp = json.loads(resp)

            timestamp = resp['props']['initialState']['note']['data']['first_shared_at']
            timestamp = time.localtime(timestamp)
            
            created_at = time.strftime("%Y-%m-%dT%H:%M:%S", timestamp)
            created_year = time.strftime("%Y", timestamp)
            updateBody = {
                "script":{
                    "inline":"ctx._source.created_at = params.created_at;ctx._source.created_year = params.created_year;",
                    "lang":"painless",
                    "params":{
                        "created_at":created_at,
                        "created_year":created_year
                    }
                }
            }
            es.update(index='article',id=id,body=updateBody)

        data = self.getSlugUrl()
        if data != False:
            print(str(self.current)+"/"+str(self.count));
            yield scrapy.Request(url=data['url'], headers=self.headers1, callback=lambda response, id=data['id']: self.parse(response, id))

