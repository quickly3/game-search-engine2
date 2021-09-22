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
    name = "juejin_daily"

    domain = 'https://juejin.cn'
    postUrl = "https://juejin.cn/post/"
    userUrl = "https://juejin.cn/user/"


    tags = [
        {"id":"6809640406058270733","tag":"设计"},
        {"id":"6809641131131797511","tag":"大数据"},
        {"id":"6809640708618584077","tag":"Kafka"},
        {"id":"6809640390522568717","tag":"PostgreSQL"},
        {"id":"6809640543006490638","tag":"TypeScript"},
        {"id":"6809640485192204295","tag":"数据可视化"},
        {"id":"6809640526904557582","tag":"数据挖掘"},
        {"id":"6809640428866895886","tag":"图片资源"},
        {"id":"6809640424882307080","tag":"创业"},
        {"id":"6809640396788858887","tag":"Docker"},
        {"id":"6809640373774712840","tag":"Git"},
        {"id":"6809640653266354190","tag":"微信小程序"},
        {"id":"6809640482725953550","tag":"程序员"},
        {"id":"6809640794794754061","tag":"Elasticsearch"},
        {"id":"6809640728428281869","tag":"Scrapy"},
        {"id":"6809640571171241998","tag":"Laravel"},
        {"id":"6809640642101116936","tag":"人工智能"},
        {"id":"6809640537583255559","tag":"React Native"},
        {"id":"6809640578855206920","tag":"Mac"},
        {"id":"6809640381920051207","tag":"Chrome"},
        {"id":"6809640505912066055","tag":"正则表达式"},
        {"id":"6809640525595934734","tag":"机器学习"},
        {"id":"6809640516439769095","tag":"黑客"},
        {"id":"6809640366896054286","tag":"MySQL"},
        {"id":"6809640540305358862","tag":"HTTP"},
        {"id":"6809640380334604295","tag":"Google"},
        {"id":"6809640411473117197","tag":"ECMAScript 6"},
        {"id":"6809640458684203021","tag":"全栈"},
        {"id":"6809640419505209358","tag":"开源"},
        {"id":"6809640392770715656","tag":"HTML"},
        {"id":"6809640467731316749","tag":"设计模式"},
        {"id":"6809640402103042061","tag":"前端框架"},
        {"id":"6809640499062767624","tag":"算法"},
        {"id":"6809640456868085768","tag":"代码规范"},
        {"id":"6809640375880253447","tag":"GitHub"},
        {"id":"6809637776909139982","tag":"Angular.js"},
        {"id":"6809640528267706382","tag":"Webpack"},
        {"id":"6809640357354012685","tag":"React.js"},
        {"id":"6809640361531539470","tag":"Node.js"},
        {"id":"6809640394175971342","tag":"CSS"},
        {"id":"6809640398105870343","tag":"JavaScript"},
        {"id":"6809640365574848526","tag":"PHP"},
        {"id":"6809640488954494983","tag":"Nginx"},
        {"id":"6809640501776482317","tag":"架构"},
        {"id":"6809640385980137480","tag":"Linux"},
        {"id":"6809640462614265863","tag":"产品经理"},
        {"id":"6809640600502009863","tag":"数据库"},
        {"id":"6809640621406421006","tag":"产品"},
        {"id":"6809640574459576334","tag":"运维"},
        {"id":"6809640408797167623","tag":"后端"},
        {"id":"6809640407484334093","tag":"前端"},
        {"id":"6809640448827588622","tag":"Python"},
        {"id":"6809641083107016712","tag":"资讯"},

    ]

    url = "https://api.juejin.cn/recommend_api/v1/article/recommend_tag_feed"

    cursor = 0


    def start_requests(self):

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        self.start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        self.end_time = self.start_time + 86400

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
            author_user_info = item['author_user_info']
            tags = item['tags']
            doc = {}
            doc['title'] = article_info['title']
            doc['url'] = self.postUrl+article_info['article_id']
            doc['summary'] = article_info['brief_content']

            doc['created_at'] = datetime.datetime.fromtimestamp(int(article_info['ctime']),None)
            doc['created_year'] = doc['created_at'].strftime("%Y")
            ts = int(article_info['ctime'])

            if ts < self.start_time :
                has_more = False;
                print("too old")
                continue;

            if ts > self.end_time :
                print("too new")
                continue;

            tagsArr = list(map(lambda x: x['tag_name'] , tags))

            doc['tag'] = tagsArr
            doc['source'] = 'juejin'
            doc['source_id'] = item['article_id']
            doc['stars'] = 0

            doc['author'] = author_user_info['user_name']
            doc['author_url'] = self.userUrl + author_user_info['user_id']


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
