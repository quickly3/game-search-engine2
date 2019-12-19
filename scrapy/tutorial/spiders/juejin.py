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
    name = "juejin"

    domain = 'https://juejin.im'

    tagId = {
        "python": "559a7227e4b08a686d25744f",
        "php": "555e9a84e4b00c57d9955e1b",
        "javascript": "55964d83e4b08a686cc6b353",
        "css": "555eadc1e4b00c57d9962402",
        "typescript": "55e7d5a360b2d687f60ae13a",
        "block_chain": "578c92bb2e958a0054375bc9",
        "game": "55e7cae700b0114357d01cb0",
        "security": "5597a500e4b08a686ce5efc3",
        "postgresql": "555e9b12e4b00c57d995654e"
    }

    tag = "python"

    urlTmpl = Template(
        "https://timeline-merger-ms.juejin.im/v1/get_tag_entry?src=web&tagId=${tagId}&page=${page}&pageSize=${pageSize}&sort=rankIndex")
    page = 0
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
            page=self.page, pageSize=self.pageSize, tagId=self._target['v'])

    def parse(self, response):
        #
        resp = json.loads(response.text)

        if len(resp['d']['entrylist']) > 0:

            bulk = []
            for item in resp['d']['entrylist']:
                doc = {}

                doc['title'] = item['title']
                doc['title_text'] = item['title']

                doc['url'] = item['originalUrl']
                doc['summary'] = item['summaryInfo']
                doc['created_at'] = item['createdAt']
                doc['created_year'] = item['createdAt']

                doc['tag'] = self.tag
                doc['source'] = 'juejin'

                doc['source_id'] = item['objectId']

                doc['stars'] = 0

                bulk.append(
                    {"index": {"_index": "article", "_type": "article"}})
                bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="article", doc_type="article",
                        body=bulk, routing=1)

            self.page = self.page+1

            url = self.get_url()
            yield scrapy.Request(url)

        else:

            if len(self.tar_arr) > 0:
                self._target = self.tar_arr.pop()
                self.page = 0
                url = self.get_url()
                yield scrapy.Request(url)

            else:
                print("Spider closeed")

            # slugs = []
            # for entity in rs['entries']:
            #     slugs.append(entity['slug'])

            # print(slugs)
