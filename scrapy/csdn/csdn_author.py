# -*- coding:UTF-8 -*-
#
#


from es.es_client import EsClient
import datetime
import scrapy
from scrapy.crawler import CrawlerProcess
import sys
import json
import pydash as _
import pprint
from pytz import timezone
from urllib.parse import urlencode
import csv

pp = pprint.PrettyPrinter(indent=4)

sys.path.append('..')


es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)


def clearHighLight(string):
    string = string.replace("<em>", "")
    string = string.replace("</em>", "")
    return string


class TestSpider(scrapy.Spider):
    name = 'csdn_author'
    domin = 'https://blog.csdn.net/'
    source = 'csdn'
    current = 0
    total = 0

    params = {
        "page": 1,
        "size": "100",
        "businessType": "blog",
        "orderby": "",
        "noMore": "false",
        "year": "",
        "month": "",
        "username": "wojiushiwo987",
    }
    baseUrl = 'https://blog.csdn.net/community/home-api/v1/get-business-list?'

    def getParams(self, option):
        self.params['page'] = option['page']
        return urlencode(self.params)

    def start_requests(self):

        option = {
            "page": 1,
            "username": "wojiushiwo987"
        }

        start_url = self.baseUrl + self.getParams(option)

        yield scrapy.Request(start_url, headers=self.headers, callback=lambda response, option=option: self.parse(response, option))

    def parse(self, response, option):

        if response.status != 200:
            yield self.getNextQuery(option, True)

        vlist = []
        # pp.pprint(response.text)
        try:
            vlist = _.get(json.loads(response.text), 'data.list.vlist')
        except ValueError as e:
            print('Error vlist 1')

        if vlist and len(vlist) > 0:
            self.itemsImport(vlist, option)
            yield self.getNextQuery(option)
        else:
            pp.pprint(response.text)
            print('Next vlist 2')
            yield self.getNextQuery(option, True)

    def itemsImport(self, items, option):
        bulk = []
        for item in items:
            doc = {}

            doc['title'] = item['title']
            print(doc['title'])
            doc['url'] = self.domin + item['bvid']
            doc['sub_id'] = item['aid']
            doc['author'] = item['author']
            doc['author_url'] = self.author_url_t.replace(
                '{mid}', str(option['mid']))
            doc['source_id'] = option['mid']
            doc['source'] = self.source
            doc['summary'] = item['description']
            date_time_obj = datetime.datetime.fromtimestamp(item['created'])
            doc['created_at'] = date_time_obj.astimezone(
                timezone("UTC")).strftime("%Y-%m-%dT%H:%M:%SZ")
            doc['created_year'] = date_time_obj.strftime("%Y")

            doc['view_count'] = item['play']
            doc['length'] = item['length']
            doc['comment_count'] = item['comment']

            # break
            bulk.append(
                {"index": {"_index": "article"}})
            bulk.append(doc)

        if len(bulk) > 0:
            resp = self.es.client.bulk(body=bulk)

    def getNextQuery(self, option, next_up=False):
        option['pn'] = option['pn'] + 1

        if next_up:
            option['mid'] = self.getNextMid(option['mid'])
            option['pn'] = 1
            if not option['mid']:
                return False

        url = self.baseUrl + self.getParams(option)
        return scrapy.Request(url, headers=self.headers, callback=lambda response, option=option: self.parse(response, option))


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
