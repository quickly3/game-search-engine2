# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import time
import datetime

from string import Template

class AliSpider(scrapy.Spider):
    # 593
    name = "bnb"

    def start_requests(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
            "pragma": "no-cache"
        }

        url = "https://www.dnb.com/business-directory/top-results.html?term=titanhouse%20inc&page=1"
        meta_proxy = "http://127.0.0.1:8181"
        yield scrapy.Request(url,headers=self.headers)

    def parse(self, response):
        print(response.text)