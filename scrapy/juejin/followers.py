import json
import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient
import urllib.parse as urlparse


class TestSpider(scrapy.Spider):
    name = 'followers'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    toCSV = []

    source = 'juejin'
    api_url = 'https://api.juejin.cn/user_api/v1/follow/followers?aid=2608&uuid=6999185118360520227';

    user_page = 'https://juejin.cn/user/'
    current = 0
    
    def updateParams(self,params):
        url_parse = urlparse.urlparse(self.api_url)
        query = url_parse.query
        url_dict = dict(urlparse.parse_qsl(query))
        url_dict.update(params)
        url_new_query = urlparse.urlencode(url_dict)
        url_parse = url_parse._replace(query=url_new_query)
        new_url = urlparse.urlunparse(url_parse)
        return new_url
        
    
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
                    "user_id": user_id,
                    "cursor":'0',
                    "limit":20
                }
                new_url = self.updateParams(payload)
                yield scrapy.Request(new_url, callback=lambda response, payload=payload : self.parse(response, payload))

    def parse(self, response, payload):
        rs = json.loads(response.text)
        _data = rs['data']
        has_more = False
        user_id = payload["user_id"]
        
        if _data is not None:
            data = rs['data']['data']
            has_more = rs['data']['hasMore']
            cursor = str(rs['data']['cursor'])
            
            tag_list = list(map(lambda x:{
                "source":"juejin", 
                "user_id":user_id, 
                # "followee_id":x["user_id"]
                "follower_id":x["user_id"]
            }, data))

            bulk = []
            
            for tag in tag_list:
                bulk.append(
                    {"index": {"_index": "followers"}})
                bulk.append(tag)
            self.es.client.bulk( body=bulk)

        if has_more == True:
            payload['cursor'] = cursor
            new_url = self.updateParams(payload)
            yield scrapy.Request(new_url, callback=lambda response, payload=payload : self.parse(response, payload))
        else:
            print(user_id + "Crawler end");


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
