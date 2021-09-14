import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from es_client import EsClient

class TestSpider(scrapy.Spider):
    name = 'juejin_upd'
    domin = 'https://juejin.cn'
    handle_httpstatus_list = [404, 500]
    # list = []
    count = 0

    def start_requests(self):
        file = 'query.csv'
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)
            for item in _list:
                url = item['url']
                # url = url.replace('juejin.im', 'juejin.cn')

                if url.find('juejin.im') == -1 and url.find('juejin.cn') == -1:
                    continue;
                else:
                    yield scrapy.FormRequest(url=url, callback=lambda response, item=item : self.parse(response, item))



    def parse(self, response, item):
        self.count+=1
        if response.status == 404:
            resp = EsClient().deleteById(item['id'])
        else:
            if response.url.find("juejin.cn/news") > -1:
                user_url = response.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/div[1]/div[1]/a[1]/@href').get()
                author = response.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/div[1]/div[1]/a[1]/text()').get()

            else:
                user_url = response.xpath('//a[@class="username username ellipsis"][1]/@href').get()
                author = response.xpath('//a[@class="username username ellipsis"][1]/text()').get()

            # if user_url is None:
            #     user_url = response.xpath('//a[@class="user-item item"][1]/@href').get()

            if user_url is None:
                user_url = response.xpath('//div[@itemprop="author"]/meta[@itemprop="url"]/@content').get()
                author = response.xpath('//div[@itemprop="author"]/meta[@itemprop="name"]/@content').get()

            if user_url is not None:
                if user_url.find(self.domin) == -1:
                    author_url = self.domin + user_url
                else:
                    author_url = user_url
                body = {
                    "doc":{
                        "author_url": author_url.strip(),
                        "author": author.strip(),
                        "url": response.url,
                    }
                }

                resp = EsClient().updateById(item['id'], body)

        print(str(self.count)+"/"+str(self.total))


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
