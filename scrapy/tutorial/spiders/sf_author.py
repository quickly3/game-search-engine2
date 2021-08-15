import scrapy
import json
import datetime
import os
from string import Template

from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

es_logger.setLevel(50)
es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))

class SfAuthorSpider(scrapy.Spider):
    name = 'sf_author'

    urlTpl = Template('https://gateway.segmentfault.com/homepage/xiaoyusmd/timeline?size=20&offset=$offset')

    offset = '';
    source = 'sf'
    domain = 'https://segmentfault.com/'


    def start_requests(self):
        url = self.urlTpl.substitute(offset=self.offset)
        yield scrapy.Request(url, method='GET')

    def parse(self, response):

        resp = json.loads(response.text)

        self.offset = resp['offset']

        print(es)

        bulk = []
        for item in resp['rows']:

            doc = {}
            doc['title'] = item['title']
            doc['url'] = self.domain+item['url']

            doc['summary'] =item['excerpt']
            # doc['tag'] = ['']
            doc['source'] = self.source

            doc['author'] = item['user']['name']
            doc['author_url'] = self.domain+item['user']['url']

            timeObj = datetime.datetime.fromtimestamp(int(item['modified']),None)

            doc['created_at'] = timeObj.strftime("%Y-%m-%d %H:%M:%S")
            doc['created_year'] = timeObj.strftime("%Y")

            doc['stars'] = 0

            print(doc)

            bulk.append(
                {"index": {"_index": "article"}})
            bulk.append(doc)

        if len(bulk) > 0:
            es.bulk(index="article", body=bulk)


        url = self.urlTpl.substitute(offset=self.offset)
        yield scrapy.Request(url, method='GET')



