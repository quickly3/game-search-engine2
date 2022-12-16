
import datetime
import scrapy
from scrapy.crawler import CrawlerProcess
import sys
import json
import pydash as _
import pprint
from pytz import timezone
from urllib.parse import urlencode

pp = pprint.PrettyPrinter(indent=4)

sys.path.append('..')
from es.es_client import EsClient

class TestSpider(scrapy.Spider):
    name = 'ups_articles'
    domin = 'https://www.bilibili.com/video/'
    source = 'bilibili'
    current = 0
    total = 0

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

    author_url_t = 'https://space.bilibili.com/{mid}'
    refer_url_t = 'https://space.bilibili.com/{mid}/video'
    baseUrl = "https://api.bilibili.com/x/space/wbi/arc/search?"
    headers = {
        "Accept": "text/html, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
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
        "Referer":""
    }

    def getParams(self, option):
        self.params['mid'] = option['mid']
        self.params['pn'] = option['pn']
        return urlencode(self.params)

    def getNextMid(self, mid = False):
        if not mid :
            mid = 517327498
        else: 
            mid = 123

        self.headers['referer'] = self.refer_url_t.replace('{mid}',str(mid))
        return mid

    def start_requests(self):
        self.es = EsClient()
        mid = self.getNextMid()
        option = {
            "mid": mid,
            "pn": 11
        }
        start_url = self.baseUrl + self.getParams(option)

        yield scrapy.Request(start_url, headers=self.headers, callback=lambda response, option=option: self.parse(response, option))

    def parse(self, response, option):
        vlist = []
        try:
            vlist = _.get(json.loads(response.text), 'data.list.vlist')
        except ValueError as e:
            print('Error vlist')
        
        if len(vlist) > 0:
            self.itemsImport(vlist, option)
            yield self.getNextQuery(option)
        else :
            yield self.getNextQuery(option, True)

    def itemsImport(self, items, option):
        bulk = []
        for item in items:
            doc = {}

            doc['title'] = item['title']
            doc['url'] = self.domin + item['bvid']
            doc['author'] = item['author']
            doc['author_url'] = self.author_url_t.replace('{mid}', str(option['mid']))
            doc['source_id'] = option['mid']
            doc['source'] = self.source
            doc['summary'] = item['description']
            date_time_obj = datetime.datetime.fromtimestamp(item['created'])
            doc['created_at'] = date_time_obj.astimezone(
                timezone("UTC")).strftime("%Y-%m-%dT%H:%M:%SZ")
            doc['created_year'] = date_time_obj.strftime("%Y")

            doc['view_count'] = item['play']
            # doc['digg_count'] = item['description']
            doc['comment_count'] = item['comment']
            # doc['collect_count'] = item['video_review']

            break
        #     bulk.append(
        #         {"index": {"_index": "article"}})
        #     bulk.append(doc)

        # if len(bulk) > 0:
        #     resp = self.es.client.bulk(body=bulk)

    def getNextQuery(self, option, next_up = False):
        option['pn'] =  option['pn'] + 1

        if next_up:
            option['mid'] = self.getNextMid(option['mid'])
            option['pn'] = 1

        url = self.baseUrl + self.getParams(option)
        return scrapy.Request(url, headers=self.headers, callback=lambda response, option=option: self.parse(response, option))


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
