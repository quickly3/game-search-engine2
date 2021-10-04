import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient
from scrapy.http import JsonRequest
import json
import juejin_util
import os
from scrapy import signals
import pprint




class TestSpider(scrapy.Spider):
    name = 'juejin_authors_crawl'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    toCSV = []

    source = 'juejin'
    api_url = 'https://api.juejin.cn/user_api/v1/user/get?aid=2608&user_id=${user_id}&not_self=1';
    user_page = 'https://juejin.cn/user/'
    current = 0
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


    def parse(self, response, item):
        self.current+=1
        
        print(self.current,'/',self.total)
        rs = json.loads(response.text)
        user_data = rs['data']

        if user_data is not None:
            
            data = {};
            for key in user_data:
                if user_data[key] != '':
                    valid = True

                    if key == 'university' and user_data[key]['name'] == '': 
                        valid = False
                    if key == 'major' and user_data[key]['name'] == '': 
                        valid = False
                    if key == 'tech_team' and user_data[key]['org_name'] == '': 
                        valid = False
                    if valid:
                        data[key] = user_data[key];

            data['source'] = 'juejin'
            bulk = []
            bulk.append(
                {"index": {"_index": "author"}})
            bulk.append(data)

            self.es.client.bulk( body=bulk)



if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
