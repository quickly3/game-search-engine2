

import datetime
import scrapy
import sys
import pprint
from scrapy.crawler import CrawlerProcess
import pandas as pd

pp = pprint.PrettyPrinter(indent=4)

# lv1_title,lv2_title,url
class TestSpider(scrapy.Spider):
    name = 'os_tools'
    domin = 'https://www.oschina.net'
    source = 'oschina'
    output = 'os_tools.csv'

    cates = []

    def start_requests(self):

        start_url = 'https://www.oschina.net/project'

        yield scrapy.Request(start_url)

    def parse(self, response):
        lv1_items = response.xpath(
            '//*[@id="projectCategoryMenu"]/div[contains(@class,"item")]')

        for item1 in lv1_items:
            lv1_title = item1.xpath('text()').get().strip()
            lv2_menus = item1.xpath('div/div/div/div')
            for menu in lv2_menus:
                lv2_items = menu.xpath('div/a')

                for item in lv2_items:
                    href = item.xpath('@href').get()
                    title = item.xpath('@title').get()

                    os_item = {
                        "lv1": lv1_title,
                        "title": title,
                        "url": self.domin + href
                    }

                    dfSg = pd.DataFrame([os_item])
                    dfSg.to_csv(self.output, mode='a',
                                encoding='utf-8', index=False, header=False)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
