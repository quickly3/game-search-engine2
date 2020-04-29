# -*- coding:UTF-8 -*-
#
from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

from operator import itemgetter
from itertools import groupby
import scrapy
import os
import re

# settings.py


es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)


def cont_filter(x):
    return x.replace("、", ".").replace("\n", "").strip(" ") != ""


def distinct(items):
    key = itemgetter('link')
    items = sorted(items, key=key)
    return [next(v) for _, v in groupby(items, key=key)]


class AliSpider(scrapy.Spider):
    # 593
    name = "hugua_list"
    source = "hugua"
    tag = ""
    type_list = []
    fanjuList = []
    domain = "http://www.hugua.cc"

    def start_requests(self):
        
        self.type_list = [
            {
                "type":"dianshiju",
                "url":"http://www.hugua.cc/xiju/index-657.html",
            },
            {
                "type":"dianying",
                "url":"http://www.hugua.cc/dongzuo/index-573.html",
            },
            {
                "type":"dongman",
                "url":"http://www.hugua.cc/dongman/index-614.html",
            }
        ]

        self.fanjuList = []
        self.curr = self.type_list.pop()

        yield scrapy.Request(url=self.curr['url'])

    def parse(self, resp):

        items = resp.xpath('//*[@id="primary"]/div/div[2]/ul/li')

        if len(items) > 0:
            for item in items:
                url = item.xpath('h5/a/@href').get()
                self.fanjuList.append(url)

        next_page = resp.xpath('//*[@id="primary"]/div/div[2]/div[2]/div/a[contains(text(), "下一页")]/@href').getall()

        if len(next_page) > 0:
            next_page_url = self.domain + next_page[0]

            yield scrapy.Request(url=next_page_url)
        else:

            f_path = 'E:\www\game-search-engine2\storage\csv\hugua_'+self.curr['type']+'_list.txt'
            with open(f_path, 'w') as f:
                for line in self.fanjuList:
                    f.write(self.domain+line+"\n")
            
            if len(self.type_list) > 0:
                self.fanjuList = []
                self.curr = self.type_list.pop()
                yield scrapy.Request(url=self.curr['url'])



