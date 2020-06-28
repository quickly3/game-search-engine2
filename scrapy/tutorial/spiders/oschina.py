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

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
# es_logger.setLevel(50)

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


# class Game(Base):
#     __tablename__ = 'EsDaily'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(200))
#     link = Column(String(200))
#     state = Column(String(200))


class AliSpider(scrapy.Spider):
    # 593
    name = "oschina"

    domain = 'https://www.oschina.net'
    # 593
    source = "oschina"

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

    urlTmpl = Template(
        'https://www.oschina.net/search?scope=blog&q=${tagId}&onlyme=0&onlytitle=0&sort_by_time=1&p=${page}')

    page = 313
    pageSize = 100
    # max_page = 0

    def start_requests(self):

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7"
        }

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
        items = response.xpath(
            './/div[has-class("search-list-container")]/div[@class="item"]')

        # if self.page == 1:
        self.max_page = response.xpath(
            './/a[has-class("page-num-item")][last()]/text()').get()
        self.max_page = int(self.max_page)

        if len(items) > 0:
            bulk = []
            for item in items:

                title_a = item.xpath('.//div[@class="content"]/h3/a')

                horizontal = title_a.xpath('.//div[has-class("horizontal")]')

                if len(horizontal) > 0:
                    horizontal = horizontal[0].root
                    horizontal.getparent().remove(horizontal)

                titles = title_a.xpath('.//text()').getall()

                title = "".join(titles)

                title = title.strip()

                url = title_a.xpath('.//@href').get()

                details = item.xpath(
                    './/div[@class="description"]/p/text()').getall()

                detail = "".join(details)
                detail = detail.strip()

                createAt = item.xpath(
                    './/div[@class="extra"]/div[has-class("list")]/div[@class="item"][2]/text()').get()

                # createAt = createAt.replace("日期：", "")

                doc = {}

                doc['title'] = title

                doc['url'] = url
                doc['summary'] = detail

                if "今天" in createAt:
                    createAt = createAt.replace("今天", self.today)

                if "昨天" in createAt:
                    createAt = createAt.replace("昨天", self.yesterday)

                if "前天" in createAt:
                    createAt = createAt.replace("前天", self.last2day)

                _date = dateparse(createAt)

                doc['created_at'] = _date.strftime("%Y-%m-%d")

                year = _date.year

                doc['created_year'] = year

                doc['tag'] = self._target['k']
                doc['source'] = self.source

                doc['stars'] = 0

                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="article", body=bulk)

        if (self.page == self.max_page) or (len(items) == 0):
            if len(self.tar_arr) > 0:
                self._target = self.tar_arr.pop()
                self.page = 1
                url = self.get_url()
                yield scrapy.Request(url)

            else:
                print("Spider closeed")
        else:
            self.page = self.page+1
            url = self.get_url()
            yield scrapy.Request(url)
