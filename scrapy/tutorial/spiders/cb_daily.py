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

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random
from dateutil import parser

from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger


env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
log_level = os.getenv("ES_LOG")

es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)

class AliSpider(scrapy.Spider):
    name = "cb_daily"


    tagId = {
        "python": {
            "cid": 108696,
        },
        "design": {
            "cid": 106892,
        },
        "php": {
            "cid": 106882,
        },
        "dp": {
            "cid": 106884,
        },
        "web": {
            "cid": 106883,
        },
        "javascript": {
            "cid": 106893,
        },
        "nosql": {
            "cid": 108743,
        },
        "mysql": {
            "cid": 108712,
        },
        "postgresql": {
            "cid": 108767,
        },
        "algorithm": {
            "cid": 108741,
        },
        "opensource": {
            "cid": 108722,
        },
        "blockchain": {
            "cid": 108764,
        },
        "translate": {
            "cid": 106875,
        }
    }
    tag = "python"
    source = "cnblogs"
    tag_index = 0


    pager_url = "https://www.cnblogs.com/AggSite/AggSitePostList"

    page = 1
    pageSize = 20

    headers = {
        "Authority": "www.cnblogs.com",
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Origin": "https://www.cnblogs.com",
        "X-requested-with": "XMLHttpRequest",
        "Referer": "https://www.cnblogs.com/cate/python/",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 ,Safari/537.36"
    }

    def start_requests(self):
        self.tag_arr = []
        for tag in self.tagId:
            self.tag_arr.append(tag)

        self.tag = self.tag_arr.pop()
        self.cateId = self.tagId[self.tag]['cid']


        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        self.start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        self.end_time = self.start_time + 86400


        formdata = self.get_formdata()

        temp = json.dumps(formdata)

        url = self.pager_url
        yield scrapy.FormRequest(url=url, body=temp, method="POST", headers=self.headers)

    def next_request(self, next_tag=False):

        if next_tag == True:
            if len(self.tag_arr) == 0:
                self.crawler.engine.close_spider(self, '关闭爬虫')
            else:
                self.page = 0
                self.tag = self.tag_arr.pop()
                self.cateId = self.tagId[self.tag]['cid']

        self.page = self.page + 1
        formdata = self.get_formdata()

        temp = json.dumps(formdata)

        url = self.pager_url
        return scrapy.FormRequest(url=url, body=temp, method="POST", headers=self.headers)

    def get_formdata(self):
        return {"CategoryType": "SiteCategory", "ParentCategoryId": 2, "CategoryId": self.cateId, "PageIndex": self.page, "TotalPostCount": 4000, "ItemListActionName": "AggSitePostList"}

    def parse(self, response):

        items = response.xpath('//*[@class="post-item-body"]')
        bulk = []
        next_tag = False

        if len(items) > 0:
            for item in items:
                doc = {}

                title = item.xpath('*/a[@class="post-item-title"]/text()').get()
                url = item.xpath('*/a[@class="post-item-title"]/@href').get()

                desps = item.xpath(
                    '*/p[@class="post-item-summary"]/text()').getall()
                desp = "".join(desps)
                desp = desp.strip()

                author = item.xpath(
                    '*/a[@class="post-item-author"]/span/text()').get()
                created_at = item.xpath('*/span[@class="post-meta-item"]/span/text()').getall()

                if len(created_at) > 0:
                    created_at = created_at[0]
                    date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M')

                    doc['created_at'] = date_time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
                    doc['created_year'] = date_time_obj.strftime("%Y")

                    ts = date_time_obj.timestamp()

                    if ts < self.start_time :
                        next_tag=True
                        print("too old")
                        continue;

                    if ts > self.end_time :
                        next_tag=True
                        print("too new")
                        continue;


                    doc['title'] = title
                    doc['url'] = url
                    doc['tag'] = self.tag
                    doc['summary'] = desp
                    doc['source'] = self.source
                    doc['source_score'] = 0
                    doc['author'] = author

                    bulk.append(
                        {"index": {"_index": "article"}})
                    bulk.append(doc)

        else:
            print("Next")
            next_tag = True

        if len(bulk) > 0:
            es.bulk(index="article", body=bulk)

        yield self.next_request(next_tag)
