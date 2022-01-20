import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient
from scrapy.http import JsonRequest
import json
import juejin_util


# 根据juejin作者爬取全部文章
class TestSpider(scrapy.Spider):
    name = 'juejin_post_crawl_by_author'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    # list = []

    source = 'juejin'
    api_url = 'https://api.juejin.cn/content_api/v1/article/query_list?aid=2608';
    current = 0

    def start_requests(self):
        file = 'authors.csv'
        self.es = EsClient()

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)
            for item in _list:
                self.current = self.current+1;
                url = item['author_url']
                if url.find('juejin.im') == -1 and url.find('juejin.cn') == -1:
                    continue;
                else:
                    user_id = url.split("/").pop();

                    item['user_id'] = user_id
                    item['cursor'] = '0'

                    payload = self.getPayload(item)

                    print(self.current,'/',self.total)
                    yield JsonRequest(self.api_url, data=payload, callback=lambda response, item=item : self.parse(response, item))

    def getPayload(self,item):

        payload = {
            "cursor": item['cursor'],
            "sort_type": 2,
            "user_id":item['user_id']
        }
        return payload;

    def parse(self, response, item):

        rs = json.loads(response.text)

        item['cursor'] = str(rs['cursor'])

        items = rs['data']
        count = rs['count']

        if count == item['doc_count']:
            print("ok")
            return "ok"

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

        if len(bulk) > 0:
            self.es.client.bulk(index="article", body=bulk)

        if has_more == True:
            payload = self.getPayload(item)
            yield JsonRequest(self.api_url,data=payload, callback=lambda response, item=item : self.parse(response, item))
            
        else:

            print(item['user_id'] + "Crawler end");

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
