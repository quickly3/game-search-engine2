# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import json

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


class AliSpider(scrapy.Spider):
    # 593
    name = "infoq"

    domain = 'https://s.geekbang.org/'

    tagId = {
        "PostgreSQL": "PostgreSQL",
    }
    tag = "PostgreSQL"

    # urlTmpl = "https://www.infoq.cn/public/v1/article/getList"
    urlTmpl = "https://s.geekbang.org/api/gksearch/search"
    page = 40
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
        formdata = self.get_formdata()
        temp = json.dumps(formdata)
        print(temp)
        yield scrapy.FormRequest(url=self.urlTmpl, body=temp, method="POST", headers=self.headers)

    def get_formdata(self):
        self.page = self.page + 1
        return {"p": self.page, "q": str(self.tagId[self.tag]), "s": self.pageSize, "t": 0}
        # return {"id": "32", "size": "12", "type": "1", "score": "1572004093883"}

    def get_url(self):
        return self.urlTmpl.substitute(
            page=self.page, pageSize=self.pageSize, tagId=self.tagId[self.tag])

    def parse(self, response):

        #
        resp = json.loads(response.text)
        print()

        if len(resp['data']['list']) > 0:

            #     bulk = []
            #     for item in resp['d']['entrylist']:
            #         doc = {}

            #         doc['title'] = item['title']
            #         doc['href'] = item['originalUrl']
            #         doc['summaryInfo'] = item['summaryInfo']
            #         doc['content'] = item['content']
            #         doc['createdAt'] = item['createdAt']
            #         doc['tag'] = self.tag
            #         doc['jid'] = item['objectId']

            #         bulk.append(
            #             {"index": {"_index": "juejin", "_type": "juejin"}})
            #         bulk.append(doc)

            #     if len(bulk) > 0:
            #         es.bulk(index="juejin", doc_type="juejin",
            #                 body=bulk, routing=1)

            #     self.page = self.page+1

            #     url = self.get_url()
            #     yield scrapy.Request(url)

            # slugs = []
            # for entity in rs['entries']:
            #     slugs.append(entity['slug'])

            # print(slugs)
