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

env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# engine = create_engine("mysql+pymysql://"+DB_USERNAME+":"+DB_PASSWORD+"@localhost/Game?charset=utf8", encoding='utf-8', echo=False)
engine = create_engine("mysql+pymysql://"+DB_USERNAME+":"+DB_PASSWORD +
                       "@localhost/"+DB_DATABASE+"?charset=utf8", encoding='utf-8', echo=False)
Base = declarative_base()


Session_class = sessionmaker(bind=engine)
Session = Session_class()


class AliSpider(scrapy.Spider):
    # 593
    name = "csdn"
    source = "csdn"

    domain = 'https://juejin.im'

    tagId = {
        "python": "python",
        "php": "php",
        "javascript": "javascript",
        "css": "css",
        "typescript": "typescript",
        "block_chain": "区块链",
        "game": "游戏",
        "security": "安全",
        "postgresql": "postgresql"
    }

    tag = "python"

    urlTmpl = Template(
        'https://so.csdn.net/so/search/s.do?q=${tagId}&t=blog&p=${page}')

    page = 1
    pageSize = 100

    def start_requests(self):

        self.tar_arr = []

        for item in self.tagId:
            self.tar_arr.append({'k': item, 'v': self.tagId[item]})

        self._target = self.tar_arr.pop()

        url = self.get_url()

        yield scrapy.Request(url)

    def get_url(self):

        return self.urlTmpl.substitute(
            page=self.page, tagId=self._target['v'])

    def parse(self, response):
        #
        # resp = json.loads(response.text)
        items = response.xpath('.//dl[has-class("search-list")]')

        if len(items) > 0:

            bulk = []
            for item in items:
                title_a = item.xpath('.//div[@class="limit_width"]/a[1]')
                titles = title_a.xpath('.//text()').getall()
                title = "".join(titles)

                url = title_a.xpath('.//@href').get()
                details = item.xpath(
                    './/dd[@class="search-detail"]/text()').getall()
                detail = "".join(details)

                createAt = item.xpath(
                    './/dd[@class="author-time"]/span[@class="date"]/text()').get()

                createAt = createAt.replace("日期：", "")

                doc = {}

                doc['title'] = title

                doc['url'] = url
                doc['summary'] = detail

                doc['created_at'] = createAt
                _date = dateparse(createAt)

                year = _date.year

                doc['created_year'] = year

                doc['tag'] = self._target['k']
                doc['source'] = self.source

                doc['stars'] = 0

                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="article",
                        body=bulk)

            self.page = self.page+1
            url = self.get_url()
            yield scrapy.Request(url)

        else:

            if len(self.tar_arr) > 0:
                self._target = self.tar_arr.pop()
                self.page = 1
                url = self.get_url()
                yield scrapy.Request(url)

            else:
                print("Spider closeed")
