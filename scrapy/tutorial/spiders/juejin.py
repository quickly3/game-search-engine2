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
    name = "juejin"

    domain = 'https://juejin.cn'
    postUrl = "https://juejin.cn/post/"

    tags = [
        {"id":"6809640794794754061","tag":"Elasticsearch"}
    ]

    url = "https://api.juejin.cn/recommend_api/v1/article/recommend_tag_feed"

    cursor = 0

    def start_requests(self):

        self._target = self.tags.pop()
        payload = self.getPayload()
        yield JsonRequest(self.url,data=payload)

    def getPayload(self):
        t = time.time()
        payload = {
            "cursor": str(self.cursor),
            "id_type": 2,
            "sort_type": 300,
            "tag_ids": [self._target['id']],
        }
        return payload;

    def parse(self, response):

        rs = json.loads(response.text)
        items = rs['data']

        self.cursor = rs['cursor']

        has_more = rs['has_more']
        bulk = []

        for item in items:
            article_info = item['article_info']
            doc = {}
            doc['title'] = article_info['title']
            doc['url'] = self.postUrl+article_info['article_id']
            doc['summary'] = article_info['brief_content']

            doc['created_at'] = datetime.datetime.fromtimestamp(int(article_info['ctime']),None)
            doc['created_year'] = doc['created_at'].strftime("%Y")

            doc['tag'] = self._target['tag']
            doc['source'] = 'juejin'
            doc['source_id'] = item['article_id']
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
            if len(self.tags) > 0:
                self.cursor = 0
                self._target = self.tags.pop()
                payload = self.getPayload()
                yield JsonRequest(self.url,data=payload)
            else:
                print("Crawler end");
