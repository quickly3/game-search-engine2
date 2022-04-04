import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse

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
    
    def start_requests(self):
        
        url = "https://github.com/trending/{lang}?since={since}&spoken_language_code={spoken_language_code}"
        for language in self.languages:
            for spoken_language_code in self.spoken_language_codes:
                for since in self.sinces:
                    _url = url.replace('{lang}',language)
                    _url = _url.replace('{since}',since)
                    _url = _url.replace('{spoken_language_code}',spoken_language_code)
                    option = {
                        language:language,
                        spoken_language_code:spoken_language_code,
                        since:since
                    }
                    yield scrapy.Request(url = _url, callback=lambda response, option=option : self.parse(response, option))
                   
    def parse(self, response, option):
        articles = response.xpath('//*[@id="js-pjax-container"]/div[3]/div/div[2]/article')
        for art in articles:
            project_name = art.xpath('string(./h1/a)').get();
            url = art.xpath('./h1/a/@href').get();
            url = self.domin + url;
            
            if not project_name:
                continue;

            doc = option
            
            project_name = project_name.replace('\n','').strip()
            project_name = ' '.join(project_name.split())
            doc['project_name'] = project_name;
            
            star = art.xpath('string(./div[2]/a[1])').get();
            star = star.replace('\n','').strip()
            doc['star'] = star;
            
            fork = art.xpath('string(./div[2]/a[2])').get();
            fork = fork.replace('\n','').strip()
            doc['fork'] = fork;
            

            desp = art.xpath('string(./p)').get();
            desp = desp.replace('\n','').strip()
            doc['desp'] = desp;
            
            print(doc)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
