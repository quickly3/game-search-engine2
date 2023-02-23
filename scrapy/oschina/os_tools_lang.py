import scrapy
import pprint
from scrapy.crawler import CrawlerProcess
import pandas as pd
from urllib.parse import urlencode
import csv

pp = pprint.PrettyPrinter(indent=4)

# lang,name,url
class TestSpider(scrapy.Spider):
    name = 'os_tools_lang'
    domin = 'https://www.oschina.net'
    source = 'oschina'
    input_file = 'os_tools_lang.csv'
    output = 'os_tools_lang_list.csv'

    baseUrl = "https://www.oschina.net/project/widgets/_project_list?"
    langs = []
    params = {
        "company": "0",
        "tag": "0",
        "lang": "269",
        "os": "0",
        "sort": "time",
        "recommend": "false",
        "cn": "false",
        "weekly": "false",
        "p": 1,
        "type": "ajax",
    }
    lang_map = {}

    def getParams(self, option):
        self.params['lang'] = option['lang']
        self.params['p'] = option['p']
        return urlencode(self.params)

    def getNextLang(self, lang=False):
        if len(self.langs) > 0:
            lang = self.langs.pop()
        else:
            return False
        return lang

    def start_requests(self):
        csv_reader = csv.DictReader(
            open(self.input_file, 'r', encoding='utf-8'), delimiter=',')

        for data in csv_reader:
            lang = data['url'].replace('https://www.oschina.net/project/lang/', '')
            lang_id = lang.split("/")[0]
            lang_str = lang.split("/")[1]

            self.langs.append(lang_id)
            self.lang_map[lang_id] = lang_str;
        
        self.langs.reverse()
        lang = self.getNextLang()
        option = {
            "lang": lang,
            "p": 1
        }
        start_url = self.baseUrl + self.getParams(option)
        yield scrapy.Request(start_url, callback=lambda response, option=option: self.parse(response, option))

    def parse(self, response, option):

        if response.status != 200:
            yield self.getNextQuery(option, True)

        items = response.xpath(
            '/html/body/div[1]/div[@class="item project-item"]')

        if items and len(items) > 0:
            for item in items:
                name = item.xpath('div/h3/a/span[1]/text()').get()
                href = item.xpath('div/h3/a/@href').get()
                tool = {
                    "lang": self.lang_map[option['lang']],
                    "name": name,
                    "href": href,
                }
                dfSg = pd.DataFrame([tool])
                dfSg.to_csv(self.output, mode='a', encoding='utf-8',
                            index=False, header=False)
            yield self.getNextQuery(option)
        else:
            print('Next lang')
            yield self.getNextQuery(option, True)

    def getNextQuery(self, option, isNext=False):
        option['p'] = option['p'] + 1
        if isNext:
            option['lang'] = self.getNextLang(option['lang'])
            option['p'] = 1
            if not option['lang']:
                return False

        url = self.baseUrl + self.getParams(option)
        return scrapy.Request(url, callback=lambda response, option=option: self.parse(response, option))


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
