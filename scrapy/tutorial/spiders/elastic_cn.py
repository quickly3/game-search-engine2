# -*- coding:UTF-8 -*-
#
#

import scrapy

class AliSpider(scrapy.Spider):
    # 593
    name = "elastic_cn"
    start_urls = [
        'https://www.elastic.co/cn/blog/archive',
    ]

    page_list = []

    source = "elastic_cn"
    tag = "elastic"

    def parse(self, response):
        objs = response.css(".blog-archive-list");

        month_list = [];

        for obj in objs:
            lists = obj.css(".archive-list-heading .align-items-center a::attr(href)").getall();
            month_list = month_list + lists;
        
        month_list = list(map(lambda x: "https://www.elastic.co"+x ,month_list))
        for
        yield response.follow(next_page_a_link, callback=self.parse_month)
       
    def parse_month(self,response):
        

