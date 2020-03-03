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
from elasticsearch import Elasticsearch

es = Elasticsearch()
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


def clearHighLight(string):
    string = string.replace("<em>", "")
    string = string.replace("</em>", "")
    return string


class AliSpider(scrapy.Spider):
    # 593
    name = "infoq"

    domain = 'https://s.geekbang.org/'

    tagId = {
        "Linux": "Linux",
        # "Postgres": "Postgres",
        # "Python": "python",
        # "Php": "php",
        # "Javascript": "javascript",
        # "Typescript": "typescript",
        # "Css": "Css",
        # "Game": "游戏",
        # "Security": "安全",
        # "Node": "Node",
        # "Js": "Js",
    }
    tag = "Linux"
    source = "infoq"
    tag_index = 0

    # urlTmpl = "https://www.infoq.cn/public/v1/article/getList"
    urlTmpl = "https://s.geekbang.org/api/gksearch/search"
    page = 0
    pageSize = 20

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "s.geekbang.org",
        "Origin": "https://s.geekbang.org",
        "Pragma": "no-cache",
        "Referer": "https://s.geekbang.org/search/c=0/k=PostgreSQL/t=",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 ,Safari/537.36"
    }

    def start_requests(self):
        #     url = self.get_url()
        self.tag_arr = []
        for tag in self.tagId:
            self.tag_arr.append(tag)

        self.tag = self.tag_arr.pop()

        formdata = self.get_formdata()

        temp = json.dumps(formdata)
        yield scrapy.FormRequest(url=self.urlTmpl, body=temp, method="POST", headers=self.headers)

    def next_request(self, next_tag=False):
        time.sleep(0.3)

        if next_tag == True:
            if len(self.tag_arr) == 0:
                self.crawler.engine.close_spider(self, '关闭爬虫')
            else:
                self.page = 0
                self.tag = self.tag_arr.pop()

        self.page = self.page + 1
        formdata = self.get_formdata()
        temp = json.dumps(formdata)
        print(temp)
        return scrapy.FormRequest(url=self.urlTmpl, body=temp, method="POST", headers=self.headers)

    def get_formdata(self):

        return {"p": self.page, "q": str(self.tagId[self.tag]), "s": self.pageSize, "t": 0}
        # return {"id": "32", "size": "12", "type": "1", "score": "1572004093883"}

    def get_url(self):
        return self.urlTmpl.substitute(
            page=self.page, pageSize=self.pageSize, tagId=self.tagId[self.tag])

    def parse(self, response):
        #
        resp = json.loads(response.text)
        if resp['code'] == 0 and len(resp['data']['list']) > 0:
            bulk = []
            for item in resp['data']['list']:

                doc = {}
                doc['title'] = item['static_title']
                doc['url'] = item['content_url']
                doc['summary'] = clearHighLight(item['summary'])
                doc['created_at'] = datetime.datetime.fromtimestamp(
                    int(item['release_time']))
                doc['author'] = item['author']
                doc['tag'] = self.tag

                if self.tag == "Postgres":
                    doc['tag'] = "PostgreSQL"

                if self.tag == "Js":
                    doc['tag'] = "Javascript"

                doc['source'] = self.source
                doc['source_id'] = item['id']
                doc['source_score'] = 0

                bulk.append(
                    {"index": {"_index": "article"}})
                resp = bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="juejin", body=bulk)

            yield self.next_request()
        else:
            yield self.next_request(next_tag=True)
