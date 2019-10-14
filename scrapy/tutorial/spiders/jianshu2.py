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
# import tuorial.settings as sp_setting


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
    name = "jianshu2"

    domain = 'https://www.jianshu.com'

    def start_requests(self):
        slugs = ['22f2ca261b85', '0bab91ded569', '8c01bfa7b98a', '0690e20b7e7d', 'aa0b21cceb92',
                 'a480500350e7', '9bc3ae683403', 'bb233a70a20e', '70eae73cf556', '7847442e0728']

        url = "https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page=1"

        # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
        # Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3
        headers1 = {
            "Accept": "text/html, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
            "x-infinitescroll": "true",
            "x-requested-with": "XMLHttpRequest"

        }

        # headers2 = {
        #     "Accept": "application/json, text/javascript, */*; q=0.01",
        #     "X-Requested-With": "XMLHttpRequest",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/56.0",
        #     "Content-Type": "application/json;charset=UTF-8",
        #     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        #     "Cookie": "JSESSIONID=2D1E55287F8B056E83FD29B114FBA389"
        # }
        # frmdata = {"q": "python",
        #            "type": 'collection',
        #            "page": '1',
        #            "order_by": 'default'}

        # jianshu_headers = {
        #     "Accept": "*/*",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Cache-Control": "max-age=0, private, must-revalidate",
        #     "Connection": "keep-alive",
        #     "Host": " www.jianshu.com",
        #     "User-Agent": random.choice(USER_AGENT_LIST),
        #     "Cookie": "_m7e_session_core=6c16b4c474dc1590d1aaf0919faa5346; locale=zh-CN",
        # }

        # headers = {
        #     "Host": "www.jianshu.com",
        #     "Connection": "keep-alive",
        #     "Content-Length": "0",
        #     "Accept": "application/json",
        #     "Origin": "https://www.jianshu.com",
        #     "X-CSRF-Token": "ftkf0tgVZjazuefhOQIGxF8hErgCVcx6ZzI0rc/gW8fnLXFlCMxvrmynQDnCaxfeSazU8FzkXLnNDKC04P/n1Q==",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        #     "Referer": "https://www.jianshu.com/search?utf8=%E2%9C%93&q=%E6%9A%B4%E9%9B%B7",
        #     "Accept-Encoding": "gzip, deflate, br",
        #     "Accept-Language": "zh-CN,zh;q=0.9",

        # }
        # yield scrapy.Request(url, headers=jianshu_headers, method='POST')

        yield scrapy.Request(url, headers=headers1)

    def parse(self, response):
        print(response.text)
        titles = response.xpath(
            '//li/div/a/text()').getall()

        print(titles)

        # urls = response.xpath(
        #     '/html/body/div[1]/div/div[1]/div[2]/ul/li/div/a/@href').getall()
        # print(urls)
