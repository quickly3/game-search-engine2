import scrapy
from scrapy.crawler import CrawlerProcess
import string
import re
from csv import writer

class TestSpider(scrapy.Spider):
    name = 'linkedin_company'
    handle_httpstatus_list = [404, 500]
    url_tpl = 'https://www.linkedin.com/directory/companies/%s'
    outPut = 'linked_companies.csv'
    seedFile = 'linkedin_alpha_urls.csv'


    custom_settings = {
        "CONCURRENT_REQUESTS": 1,
        # "DOWNLOAD_DELAY" : 5,
        # "RANDOMIZE_DOWNLOAD_DELAY": True,
        "RETRY_TIMES": 10
    }

    def start_requests(self):

        wordlist = list(string.ascii_lowercase)
        wordlist.append('more')


        with open(self.seedFile, 'a') as f_object:
            writer_object = writer(f_object)
            for word in wordlist:
                url = self.url_tpl % (word)
                writer_object.writerow({url:url})

            f_object.close()

    # def parse(self, response, main):
    #     page_list = '//*[@id="main-content"]/div/ol/li';
    #     page_list_items = response.xpath(page_list)

    #     urlList = []
    #     for item in page_list_items:
    #         page_url = item.xpath("a/@href").getall()
    #         urlList.append(page_url)

    #     with open(self.outPut, 'a') as f_object:
    #         writer_object = writer(f_object)
    #         for url in urlList:
    #             writer_object.writerow(url)
    #         f_object.close()



if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
