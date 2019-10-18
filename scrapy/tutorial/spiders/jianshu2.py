# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import json
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random
from string import Template

from elasticsearch import Elasticsearch

es = Elasticsearch()
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


class AliSpider(scrapy.Spider):
    # 593
    name = "jianshu2"

    domain = 'https://www.jianshu.com'
    url_list = []
    slug_end = True

    def __init__(self):
        self.slugs = ['22f2ca261b85', '0bab91ded569', '8c01bfa7b98a', '0690e20b7e7d', 'aa0b21cceb92',
                      'a480500350e7', '9bc3ae683403', 'bb233a70a20e', '70eae73cf556', '7847442e0728',
                      '3e3636c40c41', '813a3b29d5fd', '826a1e944a7d', '3ce88fc43e68', '614849b2a5ad',
                      '24e1fbfc147f', 'd53dd7115ed7', '80fa19f59623', 'dfcf1390085c', '5da7e0427999',
                      'b0c93dd63315', '24d9279a3f1c', 'f165d63574d2', '38980843c0f2', 'e073fce5432f',
                      'f204a5f9aac5', '74c5836708df', '4719b64b55a2', '917335d52a08', '954bbd65c3b3']

        self.slugs = ['954bbd65c3b3']

        self.url_model = Template(
            "https://www.jianshu.com/c/${slug}?order_by=top&page=${page}")

        self.headers1 = {
            "Accept": "text/html, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
            "x-infinitescroll": "true",
            "x-requested-with": "XMLHttpRequest"
        }

        self.headers2 = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/56.0",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cookie": "JSESSIONID=2D1E55287F8B056E83FD29B114FBA389"
        }

        self._page = 2

        # self._page = 146
        self.slug = ""

    def getSlugUrl(self):

        if self.slug_end:

            if len(self.slugs) == 0:
                return False

            self._slug = self.slugs.pop(0)
            self.slug_end = False

        return self.url_model.substitute(slug=self._slug, page=self._page)

    def setPage(self, url):
        return url % (self._page)

    def start_requests(self):
        url = self.getSlugUrl()
        yield scrapy.Request(url, headers=self.headers1)

    def init_page_crawl(self):
        self.slug_end = True
        self.url_list = []
        self._page = 0

    def parse(self, response):

        objs = response.xpath(
            '//li/div')
        bulk = []

        if len(objs) == 0:
            self.init_page_crawl()

        for obj in objs:
            title = obj.xpath('a/text()').get()
            href = obj.xpath('a/@href').get()
            desc = obj.xpath('p/text()').get()

            if title == None:
                continue

            doc = {
                "title": title.strip(),
                "href": href,
                "desc": desc.strip()
            }

            # if href in self.url_list:
            #     self.init_page_crawl()
            #     break

            self.url_list.append(href)

            bulk.append(
                {"index": {"_index": "jianshu", "_type": "jianshu"}})
            bulk.append(doc)

        if len(bulk) > 0:
            es.bulk(index="jianshu", doc_type="jianshu",
                    body=bulk, routing=1)

        self._page = self._page+1
        url = self.getSlugUrl()

        if url != False:
            time.sleep(1)
            yield scrapy.Request(url, headers=self.headers1)
        # urls = response.xpath(
        #     '/html/body/div[1]/div/div[1]/div[2]/ul/li/div/a/@href').getall()
        # print(urls)
