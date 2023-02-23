import scrapy
import pprint
from scrapy.crawler import CrawlerProcess
import pandas as pd
from urllib.parse import urlencode
import csv

pp = pprint.PrettyPrinter(indent=4)

# tag,name,url
class TestSpider(scrapy.Spider):
    name = 'os_tools_tag'
    domin = 'https://www.oschina.net'
    source = 'oschina'
    input_file = 'os_tools_tag.csv'
    output = 'os_tools_tag_list.csv'

    baseUrl = "https://www.oschina.net/project/widgets/_project_list?"
    tags = []
    params = {
        "company": "0",
        "lang": "0",
        "tag": "0",
        "os": "0",
        "sort": "time",
        "recommend": "false",
        "cn": "false",
        "weekly": "false",
        "p": 1,
        "type": "ajax",
    }
    tag_map = {}

    def getParams(self, option):
        self.params['tag'] = option['tag']
        self.params['p'] = option['p']
        return urlencode(self.params)

    def getNextTag(self, tag=False):
        if len(self.tags) > 0:
            tag = self.tags.pop()
        else:
            return False
        return tag

    def start_requests(self):
        csv_reader = csv.DictReader(
            open(self.input_file, 'r', encoding='utf-8'), delimiter=',')

        for data in csv_reader:
            tag = data['url'].replace('https://www.oschina.net/project/tag/', '')
            tag_id = tag.split("/")[0]
            tag_str = tag.split("/")[1]

            self.tags.append(tag_id)
            self.tag_map[tag_id] = tag_str;
        
        self.tags.reverse()
        tag = self.getNextTag()
        option = {
            "tag": tag,
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
                    "tag": self.tag_map[option['tag']],
                    "name": name,
                    "href": href,
                }
                dfSg = pd.DataFrame([tool])
                dfSg.to_csv(self.output, mode='a', encoding='utf-8',
                            index=False, header=False)
            yield self.getNextQuery(option)
        else:
            print('Next tag')
            yield self.getNextQuery(option, True)

    def getNextQuery(self, option, isNext=False):
        option['p'] = option['p'] + 1
        if isNext:
            option['tag'] = self.getNextTag(option['tag'])
            option['p'] = 1
            if not option['tag']:
                return False

        url = self.baseUrl + self.getParams(option)
        return scrapy.Request(url, callback=lambda response, option=option: self.parse(response, option))


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
