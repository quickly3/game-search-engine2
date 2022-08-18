import scrapy
import pydash as _
from scrapy.crawler import CrawlerProcess
from scrapy.http import JsonRequest
from scrapy.http import Request

import json
import os
import csv
import urllib

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
            print(item)

            doc = {
                "title": _.get(item, 'title'),
                "url": _.get(item, 'post_url'),
                "author_url": _.get(item, 'post_url'),
                "summary": _.get(item, 'summary'),
                "tag": self.tag,
                "author": _.get(item, 'user_nick'),
                "source": self.source,
                "stars": 0,
                "created_at": created_at+"Z",
                "created_year": created_year,
                "view_count": _.get(item, 'view_count'),
                "valid": True
            }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
