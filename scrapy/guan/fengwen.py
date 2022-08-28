import urllib
import csv
import os
import json
import scrapy
import pydash as _
from scrapy.crawler import CrawlerProcess
from scrapy.http import JsonRequest
from scrapy.http import Request
import pprint
import time
from dateutil import parser
import datetime

pp = pprint.PrettyPrinter(indent=4)


# 导出掘金所有tags


class TestSpider(scrapy.Spider):
    name = 'guan_fengwen'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    source = 'guancha'
    api_url = 'https://user.guancha.cn/user/get-published-list'
    author_url = 'https://user.guancha.cn/user/personal-homepage'
    doc_count = 0
    page_no = 1
    uid = 253941
    isSelf = 0
    tag = '风闻'

    today = time.strftime("%Y-%m-%d")

    yesterday = (datetime.date.today() +
                 datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    last2day = (datetime.date.today() +
                datetime.timedelta(days=-2)).strftime("%Y-%m-%d")

    def getUrl(self):
        params = {
            'page_no': self.page_no,
            'uid': self.uid,
            'isSelf': self.isSelf,

        }
        params_str = urllib.parse.urlencode(params, doseq=True)
        url = self.api_url + '?' + params_str
        return url

    def start_requests(self):
        url = self.getUrl()
        yield Request(url)

    def parse(self, response):
        resp = json.loads(response.text)
        items = _.get(resp, 'data.items')

        for item in items:

            created_at = item['created_at']

            if "分钟前" in created_at:
                created_at = self.today

            if "小时前" in created_at:
                created_at = self.today

            if "昨天" in created_at:
                created_at = self.yesterday

            created_at = parser.parse(created_at)

            created_at_str = created_at.strftime("%Y-%m-%dT%H:%M:%SZ")
            created_year_str = created_at.year


            doc = {
                "title": _.get(item, 'title'),
                "url": _.get(item, 'post_url'),
                "author_url": _.get(item, 'post_url'),
                "summary": _.get(item, 'summary'),
                "tag": self.tag,
                "author": _.get(item, 'user_nick'),
                "source": self.source,
                "stars": 0,
                "created_at": created_at_str,
                "created_year": created_year_str,
                "view_count": _.get(item, 'view_count'),
                "valid": True
            }
            
            pp.pprint(doc)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
