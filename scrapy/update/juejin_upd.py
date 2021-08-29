import scrapy
from scrapy.crawler import CrawlerProcess
from es_client import EsClient



class TestSpider(scrapy.Spider):
    name = 'juejin_upd'
    domin = 'https://juejin.cn'

    def start_requests(self):
        
        self.es = EsClient()
        scrollResp = self.es.getDocs()

        url = scrollResp['hits'][0]['url']
        scroll_id = scrollResp['scroll_id']

        yield scrapy.FormRequest(url=url, callback=lambda response, scroll_id=scroll_id : self.parse(response, scroll_id))



    def parse(self, response, scroll_id):

        author_url = self.domin + response.xpath('//a[@class="avatar-link"][1]/@href').get()
        
        print('author_url')
        print(author_url)
        


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()