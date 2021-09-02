import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient

class TestSpider(scrapy.Spider):
    name = 'juejin_author_crawl'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    # list = []
    count = 0

    def start_requests(self):
        file = 'authors.csv'
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)
            for item in _list:
                url = item['author_url']+'/posts'
                if url.find('juejin.im') == -1 and url.find('juejin.cn') == -1:
                    continue;
                else:
                    yield scrapy.FormRequest(url=url, callback=lambda response, item=item : self.parse(response, item))


    def parse(self, response, item):
        items = response.xpath('//*[@id="juejin"]/div[1]/main/div[3]/div[1]/div[2]/div/div[2]/div/ul/div/li[1]/div/div/div/div')

        for item in items:
            title = item.xpath('div[2]/div/div[1]/a/span/text()').get()
            url = item.xpath('div[2]/div/div[1]/a/@href)').get()

            print(title)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
