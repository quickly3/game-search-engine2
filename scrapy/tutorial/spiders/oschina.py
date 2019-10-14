# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# settings.py
from dotenv import load_dotenv
from pathlib import Path
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

    def start_requests(self):
        url = "https://www.oschina.net/project/tags"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7"
        }

        yield scrapy.http.Request(url, headers=headers)

    def parse(self, response):
        category_items = response.xpath(
            '/html/body/div[3]/div[3]/div/div/div[3]/div/div/div')
        for item in category_items:
            print(item.xpath('./div/div/h3/text()').get())
