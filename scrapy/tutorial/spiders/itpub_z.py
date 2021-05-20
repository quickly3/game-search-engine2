# -*- coding:UTF-8 -*-
#
#

import scrapy
import os

from string import Template
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

env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

class AliSpider(scrapy.Spider):
    # 593
    name = "itpub_z"

    domain = 'https://z.itpub.net/'
    # 593
    source = "itpub"

    page = 1
    pageSize = 100

    def start_requests(self):
        url = 'https://z.itpub.net'

        yield scrapy.Request(url)

    def parse(self, response):
        items = response.xpath('/html/body/div[3]/div[1]/div[4]/ul/li')

        bulk = []
        for item in items:
            doc = {}
            doc['title'] = item.xpath("a/div/div[2]/h4/text()").get();
            if not doc['title']:
                doc['title'] = item.xpath("a/div/div/h4/text()").get();

            print(doc)

            # doc['url'] = "https://www.elastic.co"+blog['url']
            # doc['created_at'] = blog['publish_date']

            # date = parser.parse(doc['created_at'])

            # doc['created_year'] = date.strftime("%Y")

            # doc['summary'] = blog['abstract_l10n']
            # doc['source'] = "elastic"
            # doc['tag'] = blog['category'][0]['title']

            # auths = list(map(lambda x: x['title'] ,blog['author']))

            # if len(auths) >0:
            #     doc['author'] = "•".join(auths)

            # bulk.append(
            #     {"index": {"_index": "article"}})
            # bulk.append(doc)