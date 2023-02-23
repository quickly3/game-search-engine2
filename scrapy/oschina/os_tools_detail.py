import scrapy
import pprint
from scrapy.crawler import CrawlerProcess
import pandas as pd
from urllib.parse import urlencode
import csv
import os

# title,subTitle,url,tag,category,protocol,location,isOS,system,sumary

pp = pprint.PrettyPrinter(indent=4)

class TestSpider(scrapy.Spider):
    name = 'os_tools_tag'
    domin = 'https://www.oschina.net'
    source = 'oschina'
    input_file = 'os_tools_list.csv'
    output = 'os_tools_detail.csv'
    tag_map = {}

    title_map = {
        '开发语言': "lang",
        '所属分类': "cate",
    }

    handle_httpstatus_list = [404, 403]

    # headers = {
    #     "Accept": "text/html, */*; q=0.01",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
    #     "Cache-Control": "no-cache",
    #     "Connection": "keep-alive",
    #     "Host": "www.oschina.net",
    #     "Pragma": "no-cache",
    #     "Referer": "https://www.oschina.net/search?scope=blog&q=python&onlyme=0&onlytitle=0&sort_by_time=1&p=2",
    #     "Sec-Fetch-Dest": "empty",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Site": "same-origin",
    #     "X-PJAX": "true",
    #     "X-PJAX-Container": ".search-container",
    #     "X-Requested-With": "XMLHttpRequest",
    #     "Cookie": "_ga=GA1.2.186448612.1576823180; __gads=ID=9759499603a966d2:T=1587006988:S=ALNI_MaHUCvHBDV4_9p3hvYSCpQ0OHpY1A; _user_behavior_=7c8e975a-2707-44d8-93af-28d6d29010d4; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1610426992; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1610965672"
    # }

    custom_settings = {
        # "CONCURRENT_REQUESTS": 5,
        "DOWNLOAD_DELAY" : 0.5,
    }

    def start_requests(self):
        csv_reader = csv.DictReader(
            open(self.input_file, 'r', encoding='utf-8'), delimiter=',')

        output_reader = csv.DictReader(
            open(self.output, 'r', encoding='utf-8'), delimiter=',')   

        reader404 = csv.DictReader(
            open('404.csv', 'r', encoding='utf-8'), delimiter=',')   

        existed_list = []
        list404 = []

        for data in output_reader:     
            existed_list.append(data['url'])

        for data in reader404:     
            list404.append(data['url'])

        for data in csv_reader:
            start_url = data['url']

            # start_url = 'https://www.oschina.net/p/active4j-oa'
            if start_url in existed_list:
                continue

            if start_url in list404:
                continue

            # yield scrapy.Request(start_url, headers=self.headers)
            yield scrapy.Request(start_url)

    def parse(self, response):

        if response.status == 404:
            dfSg404 = pd.DataFrame([response.url])
            dfSg404.to_csv('404.csv', mode='a', encoding='utf-8',
                        index=False, header=False)
            return

        if response.status == 403:
            print('403 reach')
            os._exit(0)


        item = {}

        title_zone = response.xpath('//*[@class="header-info__title-link"]')

        item['title'] = title_zone.xpath('span[1]/text()').get()
        item['subTitle'] = title_zone.xpath('span[2]/text()').get()
        item['url'] = title_zone.xpath('@href').get()
        info_items = response.xpath('//*[@class="info-item"]')

        info = []
        tag = ''
        category = ''
        protocol = ''
        location = ''
        isOS = ''
        system = ''
        sumary = ''

        for iitem in info_items:
            label = iitem.xpath('span[1]/text()').get().strip()
            content = iitem.xpath('span[2]').xpath('string(.)').get().strip()
            # print(label)
            # print(content)

            info.append({
                'label': label,
                'content': content
            })

            if label == '开发语言':
                tag = content.replace('查看源码 »', '')
                tag = ' '.join(tag.split()).split(' ')
                tag = ','.join(tag)

            if label == '所属分类':
                category = content.split('、')
                category = list(map(lambda x: x.strip(), category))
                category = ','.join(category)

            if label == '授权协议':
                protocol = content

            if label == '地区':
                location = content

            if label == '软件类型':
                isOS = content

            if label == '操作系统':
                system = content

        sumary_content = response.xpath(
            '//*[@class="article-detail"]/div[@class="content"]')

        sumary = sumary_content.xpath('p[1]').xpath('string(.)').get()

        if (sumary is None) or sumary.strip() == '':
            sumary = sumary_content.xpath('*/p[1]').xpath('string(.)').get()

        if (sumary is None) or sumary.strip() == '':
            sumary = sumary_content.xpath('p[2]').xpath('string(.)').get() 

        if (sumary is None) or sumary.strip() == '':
            sumary = sumary_content.xpath('*/p[2]').xpath('string(.)').get()           

        if sumary:
            sumary = sumary.strip()

        if sumary is None:
            sumary = ''

        sumary = ' '.join(sumary.split())

        item['tag'] = tag
        item['category'] = category
        item['protocol'] = protocol
        item['location'] = location
        item['isOS'] = isOS
        item['system'] = system
        item['sumary'] = sumary

        print(item)

        dfSg = pd.DataFrame([item])
        dfSg.to_csv(self.output, mode='a', encoding='utf-8',
                    index=False, header=False)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
