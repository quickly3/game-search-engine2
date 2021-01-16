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
from scrapy.http import JsonRequest


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

DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine("mysql+pymysql://"+DB_USERNAME+":"+DB_PASSWORD +
                       "@localhost/"+DB_DATABASE+"?charset=utf8", encoding='utf-8', echo=False)
Base = declarative_base()


Session_class = sessionmaker(bind=engine)
Session = Session_class()


class AliSpider(scrapy.Spider):
    # 593
    name = "juejin_daily"

    domain = 'https://juejin.im'

    tagId = {
        "python": "559a7227e4b08a686d25744f",
        "php": "555e9a84e4b00c57d9955e1b",
        "javascript": "6809640398105870343",
        "css": "555eadc1e4b00c57d9962402",
        "typescript": "55e7d5a360b2d687f60ae13a",
        "blockchain": "578c92bb2e958a0054375bc9",
        "game": "55e7cae700b0114357d01cb0",
        "security": "5597a500e4b08a686ce5efc3",
        "postgresql": "555e9b12e4b00c57d995654e"
    }

    url = "https://api.juejin.cn/recommend_api/v1/article/recommend_cate_tag_feed"

    cursor = 0

    def start_requests(self):

        self.tar_arr = []

        for item in self.tagId:
            self.tar_arr.append({'k': item, 'v': self.tagId[item]})

        self._target = self.tar_arr.pop()
        
        payload = {
            "cate_id": "6809637767543259144",
            "cursor": "0",
            "id_type": 2,
            "limit": 20,
            "sort_type": 300,
            "tag_id": "6809640407484334093"
        }

        yield JsonRequest(self.url,data=payload)


    def parse(self, response):

        rs = json.loads(response.text)
        items = rs['data']

        for item in items:
            print(item['article_info'])
            doc['title'] = item['article_info']['title']


        #
        # resp = json.loads(response.text)

        # if len(resp['d']['entrylist']) > 0:

        #     bulk = []
        #     for item in resp['d']['entrylist']:
        #         doc = {}

        #         

        #         doc['url'] = item['originalUrl']
        #         doc['summary'] = item['summaryInfo']
        #         doc['created_at'] = item['createdAt']
        #         _date = dateparse(item['createdAt'])

        #         year = _date.year

        #         doc['created_year'] = year

        #         doc['tag'] = self._target['k']
        #         doc['source'] = 'juejin'

        #         doc['source_id'] = item['objectId']

        #         doc['stars'] = 0

        #         bulk.append(
        #             {"index": {"_index": "article"}})
        #         bulk.append(doc)

        #     if len(bulk) > 0:
        #         es.bulk(index="article", body=bulk)

        #     self.page = self.page+1

        #     url = self.get_url()
        #     yield scrapy.Request(url)

        # else:

            # if len(self.tar_arr) > 0:
            #     self._target = self.tar_arr.pop()
            #     self.page = 0
            #     url = self.get_url()
            #     yield scrapy.Request(url)

            # else:
            #     print("Spider closeed")

            # slugs = []
            # for entity in rs['entries']:
            #     slugs.append(entity['slug'])

            # print(slugs)