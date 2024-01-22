import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient
import json

class TestSpider(scrapy.Spider):
    name = 'juejin_authors_crawl'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    toCSV = []

    max_id = 641770521365927

    source = 'juejin'
    api_url = 'https://api.juejin.cn/user_api/v1/user/get?aid=2608&user_id=${user_id}&not_self=1';
    user_page = 'https://juejin.cn/user/'
    current = 0
    def start_requests(self):
        file = 'authors_merged.csv'
        self.es = EsClient()

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)

            for item in _list:
                user_id = item['id']

                if self.max_id != 0 and int(user_id) <= self.max_id:
                    self.current+=1
                    continue

                url = self.api_url.replace('${user_id}', user_id)
                yield scrapy.Request(url = url, callback=lambda response, item=item : self.parse(response, item))


    def parse(self, response, item):
        self.current+=1
        print(self.current,'/',self.total)

        try:
            rs = json.loads(response.text)
        except Exception as e :
            print(response.text)
            print(e)
            raise scrapy.exceptions.CloseSpider(reason="End spider")


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
