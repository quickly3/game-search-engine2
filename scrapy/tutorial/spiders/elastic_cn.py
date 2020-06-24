# -*- coding:UTF-8 -*-
#
#

import scrapy
from elasticsearch import Elasticsearch
from datetime import date,datetime
import os
import json
from dateutil import parser

# settings.py
es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")

es = Elasticsearch(http_auth=(es_user, es_pwd))


class AliSpider(scrapy.Spider):
    # 593
    name = "elastic_cn"
    start_urls = [
        'https://www.elastic.co/cn/blog/archive',
    ]

    page_list = []

    source = "elastic_cn"
    tag = "elastic"

    def parse(self, response):
        objs = response.css(".blog-archive-list");

        month_list = [];

        for obj in objs:
            lists = obj.css(".archive-list-heading .align-items-center>a::attr(href)").getall();
            month_list = month_list + lists;
        
        month_list = list(map(lambda x: "https://www.elastic.co"+x ,month_list))

        for link in month_list:
            yield response.follow(link, callback=self.parse_month)


        # link = "https://www.elastic.co/cn/blog/archive/2019/march"
        # yield response.follow(link, callback=self.parse_month)
       
    def parse_month(self, response):

        script = blogs = response.css("#__NEXT_DATA__::text").get()
        next_data = data = json.loads(script)

        blogs = next_data['props']['pageProps']['entry'][0];

        bulk = []

        for blog in blogs:
            doc = {}
            doc['url'] = "https://www.elastic.co"+blog['url']
            doc['title'] = blog['title_l10n']
            doc['created_at'] = blog['publish_date']

            date = parser.parse(doc['created_at'])

            doc['created_year'] = date.strftime("%Y")

            doc['summary'] = blog['abstract_l10n']
            doc['source'] = "elastic"
            doc['tag'] = blog['category'][0]['title']

            auths = list(map(lambda x: x['title'] ,blog['author']))

            if len(auths) >0:
                doc['author'] = "•".join(auths)

            bulk.append(
                {"index": {"_index": "article"}})
            bulk.append(doc)

        
        if len(bulk) > 0:
            resp = es.bulk(index="article", body=bulk)


