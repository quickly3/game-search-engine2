import datetime
import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
from urllib.parse import parse_qs
import os
import re
from es_client import EsClient
import pprint

pp = pprint.PrettyPrinter(indent=4)

class TestSpider(scrapy.Spider):
    name = 'trending_daily'
    domin = 'https://github.com'
    handle_httpstatus_list = [404, 500]
    toCSV = []
    source = 'github'
    current = 0
    languages = ['css','html','javascript','jupyter-notebook','python','typescript','php']
    spoken_language_codes = ['en','zh']
    sinces = ['daily','weekly','monthly']
    total = 0
    
    custom_settings = {
        "CONCURRENT_REQUESTS": 1,
        "DOWNLOAD_DELAY" : 2,
        "RANDOMIZE_DOWNLOAD_DELAY": True,
        "RETRY_TIMES": 0
    }

    def start_requests(self):
        self.es = EsClient()

        urls = [
            'https://github.com/trending?since=daily',
            'https://github.com/trending?since=weekly',
            'https://github.com/trending?since=monthly',
            'https://github.com/trending?since=daily&spoken_language_code=zh',
            'https://github.com/trending?since=weekly&spoken_language_code=zh',
            'https://github.com/trending?since=monthly&spoken_language_code=zh'
        ]
        url = "https://github.com/trending/{lang}?since={since}&spoken_language_code={spoken_language_code}"
        for language in self.languages:
            for spoken_language_code in self.spoken_language_codes:
                for since in self.sinces:
                    _url = url.replace('{lang}',language)
                    _url = _url.replace('{since}',since)
                    _url = _url.replace('{spoken_language_code}',spoken_language_code)
                    option = {
                        'language':language,
                        'spoken_language_code':spoken_language_code,
                        'since':since
                    }
                    yield scrapy.Request(url = _url, callback=lambda response, option=option : self.parse(response, option))

        for url2 in urls:
            option = {}
            yield scrapy.Request(url = url2, callback=lambda response, option=option : self.parse(response, option))
                   
    def parse(self, response, option):
        articles = response.xpath("//*[@class='Box-row']")

        parsed_url = urlparse(response.request.url)
        captured_value = parse_qs(parsed_url.query)

        if 'since' in captured_value:
            _since = captured_value['since'][0]
        else:
            _since = 'daily'

        bulk = []
        for art in articles:
            project_name = art.xpath('string(./h2/a)').get();
            url = art.xpath('./h2/a/@href').get();
            url = self.domin + url;

            regRex = re.compile('(\/[^/]+)?$')
            author_url = regRex.sub('',url)

            if not project_name:
                continue;

            doc = {}
            
            project_name = project_name.replace('\n','').strip()
            project_name = ' '.join(project_name.split())
            doc['project_name'] = project_name;

            names = project_name.split('/')
            author = names[0].strip()
            
            star = art.xpath('string(./div[2]/a[1])').get();
            star = star.replace('\n','').strip()
            
            if star == '':
                star = 0
            else:
                star = int(star.replace(',', ''))

            fork = art.xpath('string(./div[2]/a[2])').get();
            fork = fork.replace('\n','').strip()

            _language = art.xpath('string(./div[2]/span[1]/span[2])').get();
            _language = _language.replace('\n','').strip()

            if fork == '':
                fork = 0
            else:
                fork = int(fork.replace(',', ''))
            
            desp = art.xpath('string(./p)').get();
            desp = desp.replace('\n','').strip()

            doc['title'] = project_name
            doc['summary'] = desp
            doc['url'] = url
            doc['source'] = 'github'

            if 'language' in option:
                doc['tag'] = [option['spoken_language_code'],option['since']]
                doc['category'] = 'single_lan'
            else:
                doc['tag'] = [_since]
                doc['category'] = 'total_lan'

            if _language != '':
                doc['tag'].append(_language)


            doc['author'] = author
            doc['author_url'] = author_url

            current_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            doc['created_at'] = current_time

            doc['view_count'] =  0
            doc['comment_count'] = fork
            doc['digg_count'] = star
            bulk.append(
                {"index": {"_index": "article"}})
            bulk.append(doc)
            # pp.pprint(doc)

        self.total += len(bulk)
        if len(bulk) > 0:
            # print(len(bulk))
            self.es.client.bulk( body=bulk)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
