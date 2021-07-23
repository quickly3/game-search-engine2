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

class AliSpider(scrapy.Spider):
    # 593
    name = "juejin_news_daily"

    domain = 'https://juejin.cn'
    postUrl = "https://juejin.cn/news/"

    url = "https://api.juejin.cn/recommend_api/v1/news/list"

    cursor = 0

    def start_requests(self):

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        self.start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        self.end_time = self.start_time + 86400

        payload = self.getPayload()
        yield JsonRequest(self.url,data=payload)

    def getPayload(self):
        payload = {
            "cursor": str(self.cursor),
            "recommend_mode": 1,
            "sort_type": 600,
            "limit": 20,
        }
        return payload;

    def parse(self, response):

        rs = json.loads(response.text)
        items = rs['data']

        self.cursor = rs['cursor']

        has_more = rs['has_more']
        bulk = []

        for item in items:
            content_info = item['content_info']
            doc = {}
            doc['title'] = content_info['title']
            doc['url'] = self.postUrl+content_info['content_id']
            doc['summary'] = content_info['brief']

            doc['created_at'] = datetime.datetime.fromtimestamp(int(content_info['ctime']),None)
            doc['created_year'] = doc['created_at'].strftime("%Y")
            ts = int(content_info['ctime'])

            if ts < self.start_time :
                has_more = False;
                print("too old")
                continue;

            if ts > self.end_time :
                print("too new")
                continue;

            doc['tag'] = [item['category']['category_url'],"news"]
            doc['source'] = 'juejin'
            doc['source_id'] = item['content_id']
            doc['stars'] = 0
            bulk.append(
                {"index": {"_index": "article"}})
            bulk.append(doc)

        if len(bulk) > 0:
            es.bulk(index="article", body=bulk)

        if has_more == True:
            payload = self.getPayload()
            yield JsonRequest(self.url,data=payload)
        else:
            print("Crawler end");

