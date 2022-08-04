from urllib.request import Request
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import JsonRequest
import json
import os
import csv

# 导出掘金所有tags
class TestSpider(scrapy.Spider):
    name = 'guan_fengwen'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    source = 'guancha'
    api_url = 'https://user.guancha.cn/user/get-published-list?page_no=1&uid=253941&isSelf=0';
    cursor = '0'
    tags = []
    doc_count = 0

    def start_requests(self):
        yield scrapy.Request(self.api_url)

    def parse(self, response):
        print(response.text)



if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
