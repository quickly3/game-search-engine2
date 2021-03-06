# -*- coding:UTF-8 -*-
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

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random
from string import Template

from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

import numpy as np

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)

env_path = Path('..')/'.env'

class AliSpider(scrapy.Spider):
    # 593
    name = "jianshu2"

    domain = 'https://www.jianshu.com'
    url_list = []
    slug_end = True

    def __init__(self):
        fileName = 'jianshu_slugs.npy'
        self.slugs = np.load(fileName, allow_pickle=True).item()

        self.collection = [];
        for tag in self.slugs:
            self.collection.append({
                "tag":tag,
                "slugs":self.slugs[tag]
            })

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

        self._page = 1

        self._coll = self.collection.pop(0)

    def getSlugUrl(self):

        if self.slug_end:

            if len(self._coll['slugs']) == 0:
                if len(self.collection) == 0:
                    self.crawler.engine.close_spider(self, '关闭爬虫')
                else:
                    self._coll = self.collection.pop(0)

            self._slug = self._coll['slugs'].pop(0)
            self.slug_end = False

        self._page = self._page+1
        return self.url_model.substitute(slug=self._slug, page=self._page)

    def start_requests(self):

        url = self.getSlugUrl()
        yield scrapy.Request(url, headers=self.headers1)

    def init_page_crawl(self):
        self.slug_end = True
        self.url_list = []
        self._page = 0

    def parse(self, response):

        objs = response.xpath(
            '//li/div')
        bulk = []

        if len(objs) == 0:
            self.init_page_crawl()

        for obj in objs:
            title = obj.xpath('a/text()').get()
            href = obj.xpath('a/@href').get()
            desc = obj.xpath('p/text()').get()
            author = obj.xpath('div/a/text()').get()

            if title == None:
                continue

            doc = {
                "title": title.strip(),
                "url": self.domain+href,
                "summary": desc.strip(),
                "tag": self._coll['tag'],
                "author": author,
                "source": "jianshu",
                "stars": 0
            }
            self.url_list.append(href)

            bulk.append(
                {"index": {"_index": "article"}})
            bulk.append(doc)

        if len(bulk) > 0:
            es.bulk(index="article",
                    body=bulk)

        url = self.getSlugUrl()

        if url != False:
            yield scrapy.Request(url, headers=self.headers1)
        else :
            print("end")
            
