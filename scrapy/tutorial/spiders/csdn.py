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

def clearHighLight(string):
    string = string.replace("<em>", "")
    string = string.replace("</em>", "")
    return string

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
        "game": "游戏",
        "security": "安全",
        "blockchain": "区块链",
        "postgresql": "postgresql"
    }

    tag = "python"

    urlTmpl = Template(
        'https://so.csdn.net/api/v2/search?q=${tagId}&t=blog&p=${page}')

    page = 2
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
        resp = json.loads(response.text)
        items = resp['result_vos']

        if len(items) > 0:
            bulk = []
            for item in items:
                doc = {}
                doc['title'] = clearHighLight(item['title'])
                doc['url'] = item['url']
                doc['summary'] = item['description']
                doc['author'] = clearHighLight(item['nickname'])

                doc['created_at'] = item['create_time_str']+"T00:00:00Z"
                doc['created_year'] = dateparse(item['create_time_str']).year

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
