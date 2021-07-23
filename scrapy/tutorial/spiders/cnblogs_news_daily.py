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

from string import Template



env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
log_level = os.getenv("ES_LOG")

es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)


def clearHighLight(string):
    string = string.replace("<em>", "")
    string = string.replace("</em>", "")
    return string


class AliSpider(scrapy.Spider):
    # 593
    name = "cnblogs_news_daily"
    tag = "news"
    source = "cnblogs"
    pager_url = Template("https://news.cnblogs.com/n/page/$page")
    domain = "https://news.cnblogs.com"

    page = 1

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

    def getUrl(self):
        return self.pager_url.substitute(page=self.page)

    def start_requests(self):

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        self.start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        self.end_time = self.start_time + 86400

        url = self.getUrl()
        yield scrapy.FormRequest(url=url, method="POST", headers=self.headers)

    def next_request(self):
        self.page = self.page + 1
        url = self.getUrl()
        return scrapy.FormRequest(url=url, method="POST", headers=self.headers)

    def parse(self, response):

        items = response.xpath('//*[@class="news_block"]')
        bulk = []

        has_more = True

        if len(items) > 0:
            for item in items:
                doc = {}

                title = item.xpath('*/h2[@class="news_entry"]/a/text()').get()
                url = item.xpath('*/h2[@class="news_entry"]/a/@href').get()

                desps = item.xpath(
                    '*/div[@class="entry_summary"]/text()').getall()
                if len(desps) > 1:
                    desp = desps[1].strip()
                else:
                    desp = desps[0].strip()

                author = item.xpath(
                    '*/div[@class="entry_footer"]/a/text()').get()

                created_at = item.xpath('*/div[@class="entry_footer"]/span[4]/text()').get()
                if not created_at:
                    created_at = item.xpath('*/div[@class="entry_footer"]/span[3]/text()').get()

                date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M')

                doc['created_at'] = date_time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
                doc['created_year'] = date_time_obj.strftime("%Y")

                ts = date_time_obj.timestamp();

                if ts < self.start_time :
                    has_more = False;
                    print("too old")
                    continue;

                if ts > self.end_time :
                    print("too new")
                    continue;


                doc['title'] = title
                doc['url'] = self.domain+url

                doc['tag'] = self.tag
                doc['summary'] = desp
                doc['source'] = self.source
                doc['source_score'] = 0

                doc['author'] = author.strip()

                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)
                print(title)
                print(doc['created_at'])

        if len(bulk) > 0:
            es.bulk(index="article", body=bulk)

        if self.page < 100 and has_more:
            yield self.next_request()
