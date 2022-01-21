# -*- coding:UTF-8 -*-
#
#

import scrapy
import json
from dateutil.parser import parse as dateparse
import os

# settings.py
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")


es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)


class AliSpider(scrapy.Spider):
    # 593
    name = "ali_dev"
    source = "ali_dev"

    domain = 'https://developer.aliyun.com/'

    tag = "team_learning"

    page = 1

    def start_requests(self):
        url = 'https://developer.aliyun.com/developer/api/index/listIndexFeed'
        yield scrapy.Request(url)

    def get_url(self):
        return 'https://developer.aliyun.com/developer/api/index/listIndexFeed?gmtCreated=%s&objectId=%s&bizCategory=yq-article'%(self.gmtCreated, self.objectId)

    def parse(self, response):
        resp = json.loads(response.text)
        items = resp['data']

        if len(items) > 0 or self.page < 5000:
            bulk = []
            for item in items:

                if item['moduleType'] != "article":
                    continue;

                obj = item['object']
                doc = {}
                doc['title'] = obj['title']
                doc['url'] = obj['link']
                doc['summary'] = obj['title']
                doc['author'] = obj['author']

                doc['created_at'] = obj['gmtCreated']
                doc['created_year'] = dateparse(doc['created_at']).year

                doc['source'] = self.source

                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="article",body=bulk)

            self.objectId = items[-1]['objectId']
            self.gmtCreated = items[-1]['objectCreate']
            self.page+=1
            yield scrapy.Request(self.get_url())
        else:
            os._exit(0)

