import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient
from scrapy.http import JsonRequest
import json
import juejin_util
import os
from scrapy import signals




class TestSpider(scrapy.Spider):
    name = 'juejin_author_info_crawl'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    toCSV = []

    source = 'juejin'
    api_url = 'https://api.juejin.cn/user_api/v1/user/get?aid=2608&user_id=${user_id}&not_self=1';
    user_page = 'https://juejin.cn/user/'
    def start_requests(self):
        file = 'authors.csv'
        self.es = EsClient()

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)
            for item in _list:
                user_id = item['author_url'].replace('https://juejin.cn/user/','');
                url = self.api_url.replace('${user_id}', user_id)
                yield scrapy.Request(url = url, callback=lambda response, item=item : self.parse(response, item))

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(TestSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def parse(self, response, item):

        rs = json.loads(response.text)
        user_data = rs['data']


        # user = {
        #     'user_id' : user_data['user_id'],
        #     'user_name' : user_data['user_name'],
        #     'user_url' : self.user_page + str(user_data['user_id']),
        #     'level' : user_data['level'],
        #     'power' : user_data['power'],
        #     'description' : user_data['description'],
        #     'post_article_count' : user_data['post_article_count'],
        #     'digg_article_count' : user_data['digg_article_count'],
        #     'view_article_count' : user_data['view_article_count'],
        #     'got_digg_count' : user_data['got_digg_count'],
        #     'got_view_count' : user_data['got_view_count'],
        #     'follower_count' : user_data['follower_count'],
        #     'wallet_total_bill' : user_data['wallet_total_bill']
        # }
        user_data['user_url'] = item['author_url']
        user_data['description'] = user_data['description'].strip();

        self.toCSV.append(user_data)


    def spider_closed(self, spider):

        file = 'author_info.csv'
        if os.path.exists(file):
            os.remove(file)

        self.toCSV = sorted(self.toCSV, key=lambda k: k['post_article_count'], reverse=True)

        keys = self.toCSV[0].keys()

        with open(file, 'w', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.toCSV)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
