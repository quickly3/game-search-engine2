
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
import os;

pp = pprint.PrettyPrinter(indent=4)

sys.path.append('..')
from es.es_client import EsClient


class TestSpider(scrapy.Spider):
    name = 'ups_articles'
    domin = 'https://www.bilibili.com/video/'
    source = 'bilibili'
    current = 0
    total = 0
    mids = []

    custom_settings = {
        "CONCURRENT_REQUESTS": 1,
        "DOWNLOAD_DELAY": 1,
        "RETRY_TIMES": 0
    }

    params = {
        "refresh__": "true",
        "mid": "517327498",
        "ps": "30",
        "tid": "0",
        "pn": 1,
        "keyword": "",
        "order": "pubdate",
        "order_avoided": "true",
    }

    handle_httpstatus_list = [504]

    author_url_t = 'https://space.bilibili.com/{mid}'
    refer_url_t = 'https://space.bilibili.com/{mid}/video'
    baseUrl = "https://api.bilibili.com/x/space/wbi/arc/search?"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "origin": "https://space.bilibili.com",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-PJAX": "true",
        "X-PJAX-Container": ".search-container",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": ""
    }

    def getParams(self, option):
        self.params['mid'] = option['mid']
        self.params['pn'] = option['pn']
        return urlencode(self.params)

    def getNextMid(self, mid=False):
        if len(self.mids) > 0:
            mid = self.mids.pop()
        else:
            return False

        crawled = False

        while True:
            count = self.es.getAuthorCount('bilibili', mid)
            print(mid)
            print(count)

            if count == 0:
                break
            mid = self.mids.pop()

        # if not mid :
        #     mid = 517327498
        # else:
        #     mid = 123
        self.headers['referer'] = self.refer_url_t.replace('{mid}', str(mid))
        return mid

    def start_requests(self):

        csv_reader = csv.DictReader(
            open('ups.csv', 'r', encoding='utf-8'), delimiter=',')

        for data in csv_reader:
            mid = data['url'].replace('https://space.bilibili.com/', '')
            self.mids.append(mid)

        self.mids.reverse()

        self.es = EsClient()
        mid = self.getNextMid()
        option = {
            "mid": mid,
            "pn": 1
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

            # last = self.es.getAuthorLast('bilibili')
            print(option)
            os._exit(0)
            # self.itemsImport(vlist, option)
            # yield self.getNextQuery(option)
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
