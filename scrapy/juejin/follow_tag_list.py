import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient
import json
from scrapy.http import JsonRequest

class TestSpider(scrapy.Spider):
    name = 'follow_tag_list'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    toCSV = []

    source = 'juejin'
    api_url = 'https://api.juejin.cn/interact_api/v1/follow/tag_list?aid=2608&uuid=6999185118360520227';

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
                payload = {
                    "self_user_id": user_id,
                    "cursor":'0',
                    "limit":20
                }
                
                yield JsonRequest(self.api_url, data=payload, callback=lambda response, payload=payload : self.parse(response, payload))


    def parse(self, response, payload):
        rs = json.loads(response.text)
        data = rs['data']
        has_more = rs['has_more']
        cursor = str(rs['cursor'])
        user_id = payload["self_user_id"]

        if data is not None:
            
            tag_list = list(map(lambda x:{
                "source":"juejin", 
                "user_id":user_id, 
                "tag_id":x["tag"]["tag_id"],
                "tag_name":x["tag"]["tag_name"]
            }, data))

            bulk = []
            
            for tag in tag_list:
                bulk.append(
                    {"index": {"_index": "follow_tags"}})
                bulk.append(tag)
            self.es.client.bulk( body=bulk)

        if has_more == True:
            payload['cursor'] = cursor
            yield JsonRequest(self.api_url, data=payload, callback=lambda response, payload=payload : self.parse(response, payload))
        else:
            print(user_id + "Crawler end");


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
