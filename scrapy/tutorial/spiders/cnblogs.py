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
    name = "cnblogs"

    domain = 'https://s.geekbang.org/'

    tagId = {
        # "python": {
        #     "cid": 108696,
        #     "max_page": 200
        # },
        # "design": {
        #     "cid": 106892,
        #     "max_page": 31
        # },
        # "php": {
        #     "cid": 106882,
        #     "max_page": 75
        # },
        # "dp": {
        #     "cid": 106884,
        #     "max_page": 34
        # },
        # "web": {
        #     "cid": 106883,
        #     "max_page": 82
        # },
        # "javascript": {
        #     "cid": 106893,
        #     "max_page": 200
        # },
        # "nosql": {
        #     "cid": 108743,
        #     "max_page": 19
        # },
        # "mysql": {
        #     "cid": 108712,
        #     "max_page": 85
        # },
        # "postgresql": {
        #     "cid": 108767,
        #     "max_page": 1
        # },
        "algorithm": {
            "cid": 108741,
            "max_page": 101
        },
        "opensource": {
            "cid": 108722,
            "max_page": 10
        },
        "blockchain": {
            "cid": 108764,
            "max_page": 6
        },
        "gamedev": {
            "cid": 108759,
            "max_page": 19
        },
        "translate": {
            "cid": 106875,
            "max_page": 5
        }
    }
    tag = "python"
    source = "cnblogs"
    tag_index = 0

    urlTmpl = Template("https://www.cnblogs.com/cate/${tag}/#p${page}")

    pager_url = "https://www.cnblogs.com/AggSite/AggSitePostList"

    page = 1
    pageSize = 20

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

    def start_requests(self):
        #     url = self.get_url()
        self.tag_arr = []
        for tag in self.tagId:
            self.tag_arr.append(tag)

        self.tag = self.tag_arr.pop()
        self.max_page = self.tagId[self.tag]['max_page']
        self.cateId = self.tagId[self.tag]['cid']

        formdata = self.get_formdata()

        temp = json.dumps(formdata)

        # url = self.urlTmpl.substitute(tag=self.tag, page=self.page)
        url = self.pager_url
        yield scrapy.FormRequest(url=url, body=temp, method="POST", headers=self.headers)

    def next_request(self, next_tag=False):

        if next_tag == True:
            if len(self.tag_arr) == 0:
                self.crawler.engine.close_spider(self, '关闭爬虫')
            else:
                self.page = 0
                self.tag = self.tag_arr.pop()
                self.max_page = self.tagId[self.tag]['max_page']
                self.cateId = self.tagId[self.tag]['cid']

        self.page = self.page + 1
        formdata = self.get_formdata()

        temp = json.dumps(formdata)

        # url = self.urlTmpl.substitute(tag=self.tag, page=self.page)
        url = self.pager_url
        return scrapy.FormRequest(url=url, body=temp, method="POST", headers=self.headers)

    def get_formdata(self):

        return {"CategoryType": "SiteCategory", "ParentCategoryId": 2, "CategoryId": self.cateId, "PageIndex": self.page, "TotalPostCount": 4000, "ItemListActionName": "AggSitePostList"}

    def get_url(self):
        return self.urlTmpl.substitute(
            page=self.page, pageSize=self.pageSize, tagId=self.tagId[self.tag])

    def parse(self, response):

        items = response.xpath('//*[@class="post_item_body"]')

        bulk = []

        next_tag = False

        if str(self.max_page) == str(self.page):
            next_tag = True

        if len(items) > 0:
            for item in items:

                title = item.xpath('h3/a/text()').get()
                url = item.xpath('h3/a/@href').get()

                desp = item.xpath(
                    'p[@class="post_item_summary"]/text()').get()

                author = item.xpath(
                    'div/a/text()').get()
                created_at = item.xpath('div/text()').getall()

                created_at = created_at[1]
                created_at = str.strip(created_at.replace("发布于", ""))

                doc = {}
                doc['title'] = title
                doc['title_text'] = title
                doc['url'] = url

                doc['tag'] = self.tag
                doc['summary'] = desp
                doc['source'] = self.source
                doc['source_score'] = 0
                doc['createdAt'] = created_at
                doc['author'] = author
                print(doc)
                os._exit(0)
                bulk.append(
                    {"index": {"_index": "article", "_type": "article"}})
                bulk.append(doc)
        else:
            print("Next")
            next_tag = True

        if len(bulk) > 0:
            resp = es.bulk(index="article", doc_type="article",
                           body=bulk, routing=1)

        yield self.next_request(next_tag)