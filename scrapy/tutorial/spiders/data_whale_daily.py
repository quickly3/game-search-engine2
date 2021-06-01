# -*- coding:UTF-8 -*-
#
#

import scrapy
import json
from dateutil.parser import parse as dateparse
import re
import os
import time
import datetime

# settings.py
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)


class AliSpider(scrapy.Spider):
    # 593
    name = "data_whale_daily"
    source = "data_whale"

    domain = 'http://datawhale.club'

    tag = "team_learning"

    page = 1

    category = {
        "5":"组队学习",
        "21":"LeetCode",
        "1":"未分类",
        "24":"深度推荐模型",
        "12":"Pandas",
        "13":"SQL",
        "17":"Go",
        "15":"推荐系统实践"
    }

    def start_requests(self):
        yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        self.start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))

        yield scrapy.Request(self.get_url())

    def get_url(self):
        return 'http://datawhale.club/latest.json?no_definitions=true&page=%s'%(str(self.page))

    def parse(self, response):
        resp = json.loads(response.text)
        items = resp['topic_list']['topics']

        if len(items) > 0:
            bulk = []
            to_next = True
            for item in items:
                doc = {}
                doc['title'] = item['title']
                doc['url'] = self.domain + '/t/topic/' + str(item['id'])
                doc['summary'] = item['fancy_title']
                doc['author'] = item['last_poster_username']

                doc['created_at'] = item['last_posted_at']

                _date = dateparse(doc['created_at'])

                if _date.timestamp() < self.start_time :
                    to_next = False
                    print("too old")
                    continue;

                doc['created_year'] = dateparse(item['created_at']).year

                doc['tag'] = self.tag
                category_id = str(item['category_id'])

                if category_id in self.category:
                    doc['tag'] = self.category[category_id]
                else :
                    doc['tag'] = "未分类"


                doc['source'] = self.source

                doc['stars'] = 0

                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="article",body=bulk)

            if to_next:
                self.page = self.page+1
                yield scrapy.Request(self.get_url())
        else:
            os._exit(0)

