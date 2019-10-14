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

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random


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
    name = "jianshu1"

    domain = 'https://www.jianshu.com'

    def start_requests(self):

        url = "https://www.jianshu.com/search/do?q=python&type=collection&page=1&order_by=default"

        jianshu_headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": " www.jianshu.com",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/533.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/533.36",
            "origin": "https://www.jianshu.com",
            "pragma": "no-cache",
            "referer": "https://www.jianshu.com/search?q=python&page=1&type=collection",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
        }

        yield scrapy.Request(url, headers=jianshu_headers, method='POST')

    def parse(self, response):

        rs = json.loads(response.text)
        slugs = []
        for entity in rs['entries']:
            slugs.append(entity['slug'])

        print(slugs)
