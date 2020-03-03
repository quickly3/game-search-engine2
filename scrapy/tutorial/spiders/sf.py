# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import time
import datetime

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
    name = "sf"

    domain = 'https://segmentfault.com/blogs/newest'
    # 593
    source = "sf"

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
        "typescript": "typescript",
        "block_chain": "区块链",
        "game": "游戏",
        "security": "安全",
        "postgresql": "postgresql",
        "linux": "linux",
        "dp": "设计模式",
        "design": "架构",
        "algorithm": "算法",
    }

    tag = "python"

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

    # urlTmpl = Template(
    #     'https://www.oschina.net/search?scope=blog&q=${tagId}&onlyme=0&onlytitle=0&sort_by_time=1&p=${page}')
    urlTmpl = Template(
        'https://segmentfault.com/search?q=${tagId}&type=article&page=${page}')

    page = 1
    pageSize = 100
    # max_page = 0

    def start_requests(self):

        self.tar_arr = []

        for item in self.tagId:
            self.tar_arr.append({'k': item, 'v': self.tagId[item]})

        self._target = self.tar_arr.pop()

        url = self.get_url()

        yield scrapy.Request(url, headers=self.headers)

    def get_url(self):

        return self.urlTmpl.substitute(
            page=self.page, tagId=self._target['v'])

    def parse(self, response):

        items = response.xpath(
            '//*[@id="searchPage"]/div[2]/div/div[1]/section')

        if len(items) > 0:
            bulk = []
            for item in items:

                title_a = item.xpath('.//h2/a')

                titles = title_a.xpath('.//text()').getall()

                title = "".join(titles)

                title = title.strip()

                url = title_a.xpath('.//@href').get()

                details = item.xpath(
                    './/p[@class="excerpt mt10"][1]/text()').getall()

                detail = "".join(details)
                detail = detail.strip()

                doc = {}

                doc['title'] = title
                doc['url'] = "https://segmentfault.com/"+url
                doc['summary'] = detail

                doc['tag'] = self._target['k']
                doc['source'] = self.source

                doc['stars'] = 0

                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="article", body=bulk)

        if len(items) == 0:
            if len(self.tar_arr) > 0:
                self._target = self.tar_arr.pop()
                self.page = 1
                url = self.get_url()
                yield scrapy.Request(url, headers=self.headers)

            else:
                print("Spider closeed")
        else:
            self.page = self.page+1
            url = self.get_url()
            yield scrapy.Request(url, headers=self.headers)
