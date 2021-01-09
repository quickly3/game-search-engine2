# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import time
import datetime

from string import Template
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse as dateparse

# settings.py
from dotenv import load_dotenv
from pathlib import Path

from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

es_logger.setLevel(50)
es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))

class AliSpider(scrapy.Spider):
    # 593
    name = "sf3"
    
    # 593
    source = "sf"
    tags = [
        "python"
    ]
    index = 0

    headers = {
        "authority":"segmentfault.com",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "accept":"*/*",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://segmentfault.com/t/java",
        "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "cookie":"_ga=GA1.2.163780455.1574132132; __gads=ID=34af804e0bbeeaac-22bec7ea41c200ef:T=1593324349:RT=1593324349:R:S=ALNI_MbwGIiX7PCHTor_yenQLaFyFtbrXQ; PHPSESSID=k8s~77b63b519e071c5a0be577aa99227487; Hm_lvt_e23800c454aa573c0ccb16b52665ac26=1609152424,1609748565; csrfToken=W5pRlgtTjI23VfVsQhLbV_eI; _gid=GA1.2.1447978914.1610013224; _gat_gtag_UA_918487_8=1; Hm_lpvt_e23800c454aa573c0ccb16b52665ac26=1610013260"
    }

    urlTmpl = Template('https://segmentfault.com/t/${tag}')
    urlApiTpl = Template('https://segmentfault.com/api/tag/${id}/contents?start=${start}&_=005cdda93fc1850526fc1f977ac09701')

    def start_requests(self):

        self.tag = self.tags[self.index]
        url = self.get_url()

        yield scrapy.Request(url, headers=self.headers)

    def get_url(self):

        return self.urlTmpl.substitute(tag=self.tag)

    def parse(self, response):
        stream = response.xpath('//*[@id="stream"]')
        if stream != None:
            dataId = stream.xpath(".//@data-id").get()
            nextStart = stream.xpath(".//@data-nextstart").get()
            items = response.xpath('//*[@class="news__item-info"]')
            if len(items) > 0:
                bulk = []
                for item in items:
                    title = item.xpath('.//h4/a/text()').get()
                    url = item.xpath('.//h4/a/@href').get()

                    # details = item.xpath(
                    #     './/p[@class="excerpt mt10"][1]/text()').getall()

                    # detail = "".join(details)
                    # detail = detail.strip()

        #         doc = {}

        #         doc['title'] = title
        #         doc['url'] = "https://segmentfault.com/"+url
        #         doc['summary'] = detail

        #         doc['tag'] = self._target['k']
        #         doc['source'] = self.source

        #         doc['stars'] = 0

        #         bulk.append(
        #             {"index": {"_index": "article"}})
        #         bulk.append(doc)

        #     # if len(bulk) > 0:
        #         # es.bulk(index="article", body=bulk)

        # if len(items) == 0:
        #     if len(self.tar_arr) > 0:
        #         self._target = self.tar_arr.pop()
        #         self.page = 1
        #         url = self.get_url()
        #         yield scrapy.Request(url, headers=self.headers)

        #     else:
        #         print("Spider closeed")
        # else:
        #     self.page = self.page+1
        #     url = self.get_url()
        #     yield scrapy.Request(url, headers=self.headers)
