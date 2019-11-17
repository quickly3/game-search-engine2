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

        q = "区块链"
        page = 4
        version = 530+random.randint(0, 9)
        # version = 537

        # cache = "no-cache,no-cache"
        cache = ""

        url_model = Template(
            "https://www.jianshu.com/search/do?q=${q}&type=collection&page=${page}&order_by=default")
        refer_model = Template(
            "https://www.jianshu.com/search?q=${q}&page=${page}&type=collection")

        user_agent_model = Template(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/${version}.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/${version}.36")

        url = url_model.substitute(q=q, page=page)
        referer = refer_model.substitute(q=q, page=page)
        user_agent = user_agent_model.substitute(version=version)

        jianshu_headers = {
            "authority": "www.jianshu.com",
            "pragma": "no-cache",
            "cache-control": cache,
            "accept": "application/json",
            "origin": "https://www.jianshu.com",
            "user-agent": user_agent,
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "referer": referer,
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7"
        }

        yield scrapy.Request(url, headers=jianshu_headers, method='POST')

    def parse(self, response):

        rs = json.loads(response.text)
        slugs = []
        for entity in rs['entries']:
            slugs.append(entity['slug'])

        print(slugs)
