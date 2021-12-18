import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient
from scrapy.http import JsonRequest
import json
import juejin_util
import os


# 根据juejin标签爬取全部文章
class TestSpider(scrapy.Spider):
    name = 'juejin_tag_crawl'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    # list = []

    source = 'juejin'
    api_url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_tag_feed?aid=2608&uuid=7005373067380491790';

    def start_requests(self):
        file = 'tags.csv'
        self.es = EsClient()

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)
            for item in _list:
                item['cursor'] = '0'
                payload = self.getPayload(item)

                yield JsonRequest(self.api_url, data=payload, callback=lambda response, item=item : self.parse(response, item))


    def getPayload(self,item):

        payload = {
            "cursor": item['cursor'],
            "id_type": 2,
            "sort_type": 300,
            "tag_ids": [item['tag_id']]
        }
        return payload;

    def parse(self, response, item):

        rs = json.loads(response.text)

        item['cursor'] = str(rs['cursor'])

        items = rs['data']

        has_more = rs['has_more']

        if items is None:
            print("None")
            return "None"
        bulk = []

        for _item in items:
            doc = juejin_util.getJuejinDocByJsonItem(_item)

            existed = self.es.articleExisted(doc['url']);

            if not existed:
                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)
            else:
                print('Existed Url:' + doc['url'])

        if len(bulk) > 0:
            self.es.client.bulk(index="article", body=bulk)

        if has_more == True:
            payload = self.getPayload(item)
            yield JsonRequest(self.api_url,data=payload, callback=lambda response, item=item : self.parse(response, item))
        else:

            print(item['tag_id'] + "Crawler end");

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
