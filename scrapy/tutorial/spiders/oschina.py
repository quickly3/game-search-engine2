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

class AliSpider(scrapy.Spider):
    # 593
    name = "oschina"

    domain = 'https://www.oschina.net'
    # 593
    source = "oschina"

    today = time.strftime("%Y-%m-%d")
    yesterday = (datetime.date.today() +
                 datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    last2day = (datetime.date.today() +
                datetime.timedelta(days=-2)).strftime("%Y-%m-%d")

    tagId = {
        "python": "python",
        "php": "php",
        "javascript": "javascript",
        "css": "css",
        "typescript": "typescript",
        # "blockchain": "区块链",
        # "game": "游戏",
        # "security": "安全",
        # "postgresql": "postgresql",
        # "linux": "linux",
        # "dp": "设计模式",
        # "design": "架构",
        # "algorithm": "算法",
    }

    tag = "python"

    urlTmpl = Template(
        'https://www.oschina.net/search?scope=blog&q=${tagId}&onlyme=0&onlytitle=0&sort_by_time=1&p=${page}&_pjax=.search-container')

    page = 1

    headers = {
        "Accept": "text/html, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "www.oschina.net",
        "Pragma": "no-cache",
        "Referer": "https://www.oschina.net/search?scope=blog&q=python&onlyme=0&onlytitle=0&sort_by_time=1&p=2",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-PJAX": "true",
        "X-PJAX-Container": ".search-container",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "_ga=GA1.2.186448612.1576823180; __gads=ID=9759499603a966d2:T=1587006988:S=ALNI_MaHUCvHBDV4_9p3hvYSCpQ0OHpY1A; _user_behavior_=7c8e975a-2707-44d8-93af-28d6d29010d4; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1610426992; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1610965672"
    }
    
    def start_requests(self):

        self.tar_arr = []

        for item in self.tagId:
            self.tar_arr.append({'k': item, 'v': self.tagId[item]})

        self._target = self.tar_arr.pop()

        url = self.get_url()

        yield scrapy.Request(url,headers=self.headers)

    def get_url(self):

        return self.urlTmpl.substitute(
            page=self.page, tagId=self._target['v'])

    def parse(self, response):

        items = response.xpath(
            './/div[has-class("search-list-container")]/div[@class="item"]')

        self.max_page = response.xpath(
            './/a[has-class("page-num-item")][last()]/text()').get()

        if self.max_page != None:
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
                    createAt = self.today

                if "昨天" in createAt:
                    createAt = self.yesterday

                if "前天" in createAt:
                    createAt = self.last2day

                if "分钟前" in createAt:
                    createAt = self.today
                
                _date = dateparse(createAt)

                doc['created_at'] = _date.strftime("%Y-%m-%dT%H:%M:%SZ")

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
                yield scrapy.Request(url,headers=self.headers)

            else:
                print("Spider closeed")
        else:
            self.page = self.page+1
            url = self.get_url()
            yield scrapy.Request(url,headers=self.headers)
