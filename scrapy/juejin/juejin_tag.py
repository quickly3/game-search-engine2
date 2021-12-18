import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import JsonRequest
import json
import os
import csv

# 导出掘金所有tags
class TestSpider(scrapy.Spider):
    name = 'juejin_tag_crawl'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    file = 'tags.csv'
    source = 'juejin'
    api_url = 'https://api.juejin.cn/tag_api/v1/query_tag_list?aid=2608&uuid=7005373067380491790';
    cursor = '0'
    tags = []
    doc_count = 0

    def start_requests(self):

        if os.path.exists(self.file):
            os.remove(self.file)



        payload = self.getPayload();
        print('payload',payload)
        yield JsonRequest(self.api_url, data=payload)


    def getPayload(self):
        payload = {
            "cursor": self.cursor,
            "sort_type": 1,
            "limit": 20
        }
        return payload;

    def parse(self, response):

        rs = json.loads(response.text)

        self.cursor = str(rs['cursor'])

        items = rs['data']
        has_more = rs['has_more']

        if items is None:
            print("None")
            return "None"
        bulk = []

        for _item in items:
            self.tags.append({
                'tag':_item['tag']['tag_name'],
                'count':_item['tag']['post_article_count'],
                'tag_id':_item['tag_id']
            })
            self.doc_count = self.doc_count+_item['tag']['post_article_count']

        if has_more == True:
            payload = self.getPayload()
            yield JsonRequest(self.api_url,data=payload)
        else:

            toCSV = self.tags
            toCSV = sorted(toCSV, key=lambda k: k['count'], reverse=True)

            keys = toCSV[0].keys()

            with open(self.file, 'w', newline='')  as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(toCSV)

            print("dov count: "+str(self.doc_count))


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
