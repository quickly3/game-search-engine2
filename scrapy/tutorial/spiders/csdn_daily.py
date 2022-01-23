# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import json
import time
from dateutil.parser import parse as dateparse
import datetime
import re


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from string import Template

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random
from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)

def clearHighLight(string):
    string = string.replace("<em>", "")
    string = string.replace("</em>", "")
    return string

class AliSpider(scrapy.Spider):
    # 593
    name = "csdn_daily"
    source = "csdn"

    domain = 'https://juejin.im'

    tagId = {
        "python": "python",
        "php": "php",
        "javascript": "javascript",
        "css": "css",
        "typescript": "typescript",
        "game": "游戏",
        "security": "安全",
        "blockchain": "区块链",
        "postgresql": "postgresql"
    }

    tag = "python"

    # urlTmpl = Template(
    #     'https://so.csdn.net/api/v2/search?q=${tagId}&t=blog&p=${page}&s=0&tm=1&lv=-1&ft=0&l=&u=')

    urlTmpl = Template(
        'https://so.csdn.net/api/v3/search?q=${tagId}&t=blog&p=${page}&s=new&tm=0&lv=-1&ft=0&l=&u=&ct=-1&pnt=-1&ry=-1&ss=-1&dct=-1&vco=-1&cc=-1&sc=-1&akt=-1&art=-1&ca=-1&prs=&pre=&ecc=-1&ebc=-1&urw=&ia=1&platform=pc')
    
   

    page = 1
    pageSize = 100

    def start_requests(self):

        self.tar_arr = []

        for item in self.tagId:
            self.tar_arr.append({'k': item, 'v': self.tagId[item]})

        self._target = self.tar_arr.pop()

        url = self.get_url()
        
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        self.start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        self.end_time = self.start_time + 86400000

        yield scrapy.Request(url)

    def get_url(self):

        return self.urlTmpl.substitute(
            page=self.page, tagId=self._target['v'])

    def parse(self, response):
        next = False
        
        if response.text.strip() != '':
            resp = json.loads(response.text)
            items = resp['result_vos']
            if items and len(items) > 0:
                bulk = []
                for item in items:
                    doc = {}
                    doc['title'] = clearHighLight(item['title'])
                    doc['url'] = re.sub(r'\?.*','',item['url'])
                    doc['summary'] = clearHighLight(item['digest'])
                    doc['author'] = clearHighLight(item['nickname'])

                    doc['created_year'] = dateparse(item['create_time_str']).year

                    doc['tag'] = self._target['k']
                    doc['source'] = self.source

                    doc['stars'] = 0

                    ts = int(item['create_time']/1000)
                    
                    date_time_obj = datetime.datetime.fromtimestamp(ts)
                    created_at = (date_time_obj+datetime.timedelta(hours=-8)).strftime("%Y-%m-%dT%H:%M:%SZ")
                    doc['created_at'] = created_at
                    print(doc['created_at'])
                    print(item['create_time_str'])

                    
                    if ts < self.start_time:
                        next = True
                        print("Too old")
                        continue

                    if ts > self.end_time:
                        next = True
                        print("Too new")
                        continue



                    bulk.append(
                        {"index": {"_index": "article"}})
                    bulk.append(doc)

                if len(bulk) > 0:
                    es.bulk(index="article",
                            body=bulk)
            else:
                next = True
        else:
            print("Empty body")
            next = True
                
        if next:
            if len(self.tar_arr) > 0:
                self._target = self.tar_arr.pop()
                self.page = 1
                url = self.get_url()
                yield scrapy.Request(url)
            else:
                print("Spider closeed")
        else:
            self.page = self.page+1
            url = self.get_url()
            yield scrapy.Request(url)