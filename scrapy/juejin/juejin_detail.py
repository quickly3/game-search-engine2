import scrapy
from scrapy.crawler import CrawlerProcess
import csv
import json
from es_client import EsClient
from scrapy.http import JsonRequest
import os

class TestSpider(scrapy.Spider):
    name = 'juejin_upd'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    # list = []
    count = 0
    api_url = 'https://api.juejin.cn/content_api/v1/article/detail?aid=2608'

    def start_requests(self):
        file = 'query.csv'
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)
            for item in _list:
                url = item['url']
                if url.find('https://juejin.cn/post') > -1:
                    article_id = item['url'].replace('https://juejin.cn/post/','')
                    payload = self.getPayload(article_id);
                    yield JsonRequest(self.api_url, data=payload, callback=lambda response, item=item : self.parse(response, item))

                if url.find('https://juejin.cn/new') > -1:
                    yield scrapy.FormRequest(url=url, callback=lambda response, item=item : self.parseNew(response, item))              



    def getPayload(self,article_id):

        payload = {
            "article_id": article_id
        }
        return payload;


    def parse(self, response, item):
        self.count+=1
        if response.status == 404:
            EsClient().updateById(item['id'], {"doc":{"valid":False}})
        else:
            rs = json.loads(response.text)
            
            if rs['data'] is not None:
                article_info = rs['data']['article_info']
                category = ''

                if rs['data']['category'] is not None:
                    category = rs['data']['category']['category_name']
                tags = rs['data']['tags']

                tags_arr = list(map(lambda x: x['tag_name'], tags));

                body = {
                    "doc":{
                        "collect_count": article_info['collect_count'],
                        "comment_count": article_info['comment_count'],
                        "digg_count": article_info['digg_count'],
                        "view_count": article_info['view_count'],
                        "hot_index": article_info['hot_index'],
                        "user_index": article_info['user_index'],
                        "author_id": article_info['user_id'],
                        "tag":tags_arr,
                        "category":category,
                    }
                }

                resp = EsClient().updateById(item['id'], body)
            else:
                print(rs)
                print(item)
                EsClient().updateById(item['id'], {"doc":{"valid":False}})

        print(str(self.count)+"/"+str(self.total))


    def parseNew(self, response, item):
        self.count+=1
        if response.status == 404:
            EsClient().updateById(item['id'], {"doc":{"valid":False}})
        else:

            user_url = response.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/div[1]/div[1]/a[1]/@href').get()
            view_count = response.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/div[1]/div[1]/span[2]/text()').get()
            comment_count = response.xpath('//*[@id="juejin"]/div[1]/main/div/div[3]/div[2]/@badge').get()
            digg_count = response.xpath('//*[@id="juejin"]/div[1]/main/div/div[3]/div[1]/@badge').get()
            category = response.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/div[1]/div[1]/a[2]/text()').get()

            
            author_id = user_url.replace("/user/","");

            body = {
                "doc":{
                    "author_id": int(author_id),
                    "comment_count": int(comment_count),
                    "digg_count": int(digg_count),
                    "view_count": int(view_count.replace('阅读',"").strip()),
                    "category": category.strip()
                }
            }
            resp = EsClient().updateById(item['id'], body)



if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
