# -*- coding:UTF-8 -*-
#
#

import scrapy
import os
import time
import datetime
from dateutil.parser import parse as dateparse

from string import Template
from dateutil import parser


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
    name = "itpub_z_daily"

    domain = 'https://z.itpub.net'
    # 593
    source = "itpub"

    page = 1
    pageSize = 100
    start_time = 0


    def getLastRecord(self):
        body = {
            "query":{
                "query_string": {
                    "query": "source:itpub"
                }
            },
            "sort": [
                {
                    "created_at": {
                        "order": "desc"
                    }
                }
            ],
            "size": 1
        }
        resp = es.search(index="article",body=body)
        if int(resp['hits']['total']['value']) > 0:
            created_at = resp['hits']['hits'][0]['_source']['created_at']
            date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S')
            self.start_time = date_time_obj.timestamp()


    def start_requests(self):
        url = 'https://z.itpub.net/?page=%s'%(str(self.page))

        self.getLastRecord()

        yield scrapy.Request(url)
        

    def get_next_page(self):
        self.page = self.page + 1;
        return 'https://z.itpub.net/?page=%s'%(str(self.page))
        

    def parse(self, response):
        to_next = True;
        items = response.xpath('/html/body/div[3]/div[1]/div[4]/ul/li')

        if len(items) == 0:
            os._exit(0)

        bulk = []
        for item in items:
            doc = {}
            doc['title'] = item.xpath("a/div/div[2]/h4/text()").get();
            doc['url'] = self.domain + item.xpath("a/@href").get();
            doc['summary'] = item.xpath("a/div/div[2]/p/text()").get();
            doc['author'] = item.xpath("a/div/div[2]/div/span[1]/text()").get();
            # doc['author_url'] = self.domain + item.xpath("a/@href").get();

            doc['created_at'] = item.xpath("a/div/div[2]/div/span[2]/text()").get();

            if not doc['title']:
                doc['title'] = item.xpath("a/div/div/h4/text()").get();
                
            if not doc['summary']:
                doc['summary'] = item.xpath("a/div/div/p/text()").get();

            if not doc['author']:
                doc['author'] = item.xpath("a/div/div/div/span[1]/text()").get();
            if not doc['author']:
                doc['author'] = item.xpath("a/div/div/*/div/span[1]/text()").get();                
            if not doc['author']:  
                doc['author'] = item.xpath("a/div/div/*/*/div/span[1]/text()").get();
            if not doc['author']:  
                doc['author'] = item.xpath("a/div/div/*/*/*/div/span[1]/text()").get();

            if not doc['created_at']:
                doc['created_at'] = item.xpath("a/div/div/div/span[2]/text()").get();
            if not doc['created_at']:
                doc['created_at'] = item.xpath("a/div/div/*/div/span[2]/text()").get();
            if not doc['created_at']:
                doc['created_at'] = item.xpath("a/div/div/*/*/div/span[2]/text()").get();
            if not doc['created_at']:
                doc['created_at'] = item.xpath("a/div/div/*/*/*/div/span[2]/text()").get();
            
            _date = dateparse(doc['created_at'])

            if _date.timestamp() < self.start_time :
                to_next = False
                print("too old")
                continue;

            date = parser.parse(doc['created_at'])
            doc['created_at'] = date.isoformat();
            doc['created_year'] = date.strftime("%Y")
            doc['source'] = self.source
            bulk.append(
                {"index": {"_index": "article"}})
            bulk.append(doc)

        if len(bulk) > 0:
            resp = es.bulk(index="article", body=bulk)

        if to_next:
            next_page = self.get_next_page()
            yield scrapy.Request(next_page)