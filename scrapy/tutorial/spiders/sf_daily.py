# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import time
import datetime
import re

from string import Template
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse as dateparse

# settings.py
from dotenv import load_dotenv
from pathlib import Path

from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

es_logger.setLevel(50)
es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))

class AliSpider(scrapy.Spider):
    # 593
    name = "sf_daily"

    # 593
    source = "sf"
    handle_httpstatus_list = [404,503]

    today = time.strftime("%Y-%m-%d")
    yesterday = (datetime.date.today() +
                 datetime.timedelta(-1)).strftime("%Y-%m-%d")
    last2day = (datetime.date.today() +
                datetime.timedelta(-2)).strftime("%Y-%m-%d")

    tagId = {
        "python": "python",
        "php": "php",
        "javascript": "javascript",
        "css": "css",
        "typescript":   "typescript",
        "blockchain": "区块链",
        "postgresql": "postgresql",
        "linux": "linux",
        "ubuntu": "ubuntu",
        "node": "node.js",
        "html": "html",
        "html5": "html5",
        "css3": "css3",
        "ai": "人工智能",
        "npl": "自然语言处理",
        "dataprocessing": "数据挖掘",
        "bigdata": "大数据",
        "machine-learn": "机器学习",
        "deep-learn": "深度学习",
        "mysql": "mysql",
        "composer": "composer",
        "nginx": "nginx",
        "db": "数据库",
        "postgresql": "postgresql",
        "redis": "redis",
        "elasticsearch": "elasticsearch",
        "solr": "solr",
        "search-engine": "搜索引擎",
        "elastic": "elastic"
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "accept-encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "pragma": "no-cache",
        "referer": "https://segmentfault.com/search?q=python&type=article&page=1",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }

    urlTmpl = Template(
        'https://segmentfault.com/t/${tagId}/blogs?page=${page}'
        )

    page = 1
    last_tag_ts = 0
    toNextTag = False

    def start_requests(self):

        self.tar_arr = []
        for item in self.tagId:
            self.tar_arr.append({'k': item, 'v': self.tagId[item]})

        self._target = self.tar_arr.pop()
        self.getLastRecord()
        url = self.get_url()
        yield scrapy.Request(url, headers=self.headers)


    def getLastRecord(self):
        query_tpl = Template("source:sf && tag:${tag}")
        body = {
            "query":{
                "query_string": {
                    "query": query_tpl.substitute(tag=self._target['k'])
                }
            },
            "sort": [
                {
                    "created_at": {
                        "order": "desc"
                    }
                }
            ],
            "size": 1
        }
        resp = es.search(index="article",body=body)
        if int(resp['hits']['total']['value']) > 0:
            created_at = resp['hits']['hits'][0]['_source']['created_at']
            date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
            self.last_tag_ts = date_time_obj.timestamp()

    def get_url(self):

        return self.urlTmpl.substitute(
            page=self.page, tagId=self._target['v'])

    def parse(self, response):

        if response.status == 200:
            items = response.xpath(
                '//*[@class="item-wrap py-3 list-group-item"]/div[@class="content"]')
            if len(items) > 0:
                bulk = []
                for item in items:

                    title_a = item.xpath('.//h5/a')
                    titles = title_a.xpath('.//text()').getall()
                    title = "".join(titles)
                    title = title.strip()
                    url = title_a.xpath('.//@href').get()

                    createdAtZone = item.xpath('.//div/span[2]/text()').get()
                    author = item.xpath('.//div/a[2]/span/text()').get()
                    author_url = item.xpath('.//div/a[2]/@href').get()

                    createdAt = createdAtZone.strip().replace(" ","").replace("发布于","").replace("\n","")


                    isToday = re.match(r'今天', createdAt)
                    isMinAgo = re.match(r'.*分钟前.*', createdAt)
                    isCurYear = re.match(r'\d{1,2}月\d{1,2}日', createdAt)
                    isDatetime = re.match(r'\d{4}-\d{1,2}-\d{1,2}', createdAt)

                    if isToday != None:
                        createdAt = self.today + "T" +createdAt.replace("今天","") + ":00Z"

                    if isMinAgo != None:
                        min = createdAt.replace("分钟前","").strip()
                        c = time.time() - int(min) * 60
                        createdAt = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(c))
                        print(createdAt)

                    if isCurYear != None:
                        createdAt = "2021-"+createdAt
                        createdAt = datetime.datetime.strptime(createdAt, "%Y-%m月%d日")
                        createdAt = str(createdAt).replace(" 00:00:00","T00:00:00Z")

                    if isDatetime != None:
                        createdAt = createdAt+"T00:00:00Z"

                    date_time_obj = datetime.datetime.strptime(createdAt, '%Y-%m-%dT%H:%M:%SZ')
                    ts = date_time_obj.timestamp()

                    if ts < self.last_tag_ts:
                        self.toNextTag = True
                        print("Too old")
                        continue

                    # detail = item.xpath(
                    #     './/p[contains(@class,"excerpt")]/text()').get()

                    doc = {}
                    doc['title'] = title
                    doc['url'] = "https://segmentfault.com"+url
                    doc['author_url'] = "https://segmentfault.com"+author_url

                    # doc['summary'] = detail
                    doc['tag'] = self._target['k']
                    doc['source'] = self.source
                    doc['author'] = author
                    doc['created_at'] = createdAt
                    doc['stars'] = 0

                    bulk.append(
                        {"index": {"_index": "article"}})
                    bulk.append(doc)

                if len(bulk) > 0:
                    es.bulk(index="article", body=bulk)

            if (len(items) == 0) or self.toNextTag:
                self.toNextTag = False
                if len(self.tar_arr) > 0:
                    self._target = self.tar_arr.pop()
                    self.getLastRecord()

                    self.page = 1
                    url = self.get_url()
                    yield scrapy.Request(url, headers=self.headers)

                else:
                    print("Spider closeed")
            else:
                self.page = self.page+1
                url = self.get_url()
                yield scrapy.Request(url, headers=self.headers)

