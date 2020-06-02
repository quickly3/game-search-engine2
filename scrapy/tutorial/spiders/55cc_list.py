# -*- coding:UTF-8 -*-
#

from operator import itemgetter
from itertools import groupby
import scrapy
import os


# settings.py


class AliSpider(scrapy.Spider):
    # 593
    name = "55cc_list"
    source = "hugua"
    tag = ""
    type_list = []
    fanjuList = []
    domain = "https://www.55cc.cc"

    def start_requests(self):
        
        self.type_list = [
            {
                "type":"dongman",
                "url":"https://www.55cc.cc/dongman/",
            }
        ]

        self.curr = self.type_list.pop()

        yield scrapy.Request(url=self.curr['url'])

    def parse(self, resp):

        items = resp.xpath('//*[@id="primary"]/div/div[2]/ul/li')

        if len(items) > 0:
            for item in items:
                url = item.xpath('h5/a/@href').get()
                self.fanjuList.append(url)

        next_page = resp.xpath('//*[@id="primary"]/div/div[2]/div[2]/div/a[contains(text(), "下一页")]/@href').getall()

        if len(next_page) > 0:
            next_page_url = self.domain + next_page[0]

            yield scrapy.Request(url=next_page_url)
        else:

            f_path = '../storage/csv/55cc_'+self.curr['type']+'_list.txt'
            with open(f_path, 'w') as f:
                for line in self.fanjuList:
                    f.write(self.domain+line+"\n")
            
            if len(self.type_list) > 0:
                self.fanjuList = []
                self.curr = self.type_list.pop()
                yield scrapy.Request(url=self.curr['url'])


