# -*- coding:UTF-8 -*-
#
#
import scrapy
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
import json

class AliSpider(scrapy.Spider):
    # 593
    name = "linkedin"

    companies = [
        'InceptionPad',
        'Bergen Community College','BoxTone Inc','24 Hour Fitness','2U','3Com Corporation',
        '3S Media','522 Productions','A-Town Bar and Grill','Abbott Laboratories/Quintiles Commercial',
        'Abercrombie & Fitch','Absolute Software','Abstract','Accents by Design','Accenture',
        'Access Funding, LLC','ACE Hardware Corporation','Fortren Funding LLC','Acendre',
        'Achieved Solutions','Acquia','Acterna','Actian, Corporation','Actuate (opentext)',
        'Acuity Audio Visual','AD PAGES MARKETING','ADF Solutions, Inc','Adobe','Adrian College',
        'American University','BaseInfoSec','Adtran','Advance Business Systems',
        'Advanced & Emerging Technologies','Advanced Computer Concepts','Advantage Green, Inc',
        'Advantech','AECOM, Inc','AEG Worldwide','Aerva, Inc','Aether Systems'
    ]

    # companies = ['InceptionPad']

    headers = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'Referer': 'https://www.google.com/',
        'cookie': 'lang=v=2&lang=en-us; bcookie="v=2&91d45281-1f21-43d9-84e9-183c8bf716ad"; bscookie="v=1&20210330020956e5ace4fe-1baf-453c-8d74-62bb2a8d1064AQGUgARAJf_mAvWqgIzgsyxovJf4XyDd"; lidc="b=TGST07:s=T:r=T:a=T:p=T:g=2035:u=1:i=1617070196:t=1617156596:v=2:sig=AQH_FOsnR-KOnKVeNQrmRH2yt7QPu161"; rtc=AQFgyE0UJ0uaCgAAAXiA5QUgndws0bMsTXVk0I2qGtLZrpU9Gz19zGrhdvCcfxfAQOIbfrY7ZLJEZ2SQMMY1ljXgOJJa4bTSDuQ0WGIC3fJDvopwZfyw0WlhKEfL3rjuUOgwFoo6MPseR-WgFIyV9uvt5AJOKYsejs-XdawBMQyCGjcvKD3OF8OQzeYzHYa424nXHpJ4KtR9sJNKQWGGhsQeYV8Nct6JwK3nxe5zlFQVmnkTz98zuXCD2A==; JSESSIONID=ajax:8936973522684550241; _ga=GA1.2.870593564.1617070202; _gid=GA1.2.444022753.1617070202; fid=AQHOLdN0jL5YiAAAAXiA5e1hzq4lrJ57o_xLW3uny4IjZBr8lNIAwBI9M-3VG2FmHPYEEELEjYfzJQ; fcookie=AQGuqd7HSYMI1QAAAXiA5gbuoxZiFlDRmX6L3qFKVFUxVjwJighxxlZERYFMhxwHfZdpFaYpeNQOJtwy_p7usB5GfbHCTwyRWi_xs8JkVKpuUZhqkphaa3ACiyoVn62AIcumBnpmKYbWEekalA97aWQvsUV68GC-vn-c0_M34lkHfxHcVi4BDPdD27BYp-ZCUqb4jWvamZ4d58aSTi_ez6iy01EV8q2qAzslrcfmTiCHWFpsVFA3_wqFN7neO1odOzCYCpgBcQbI8h-5N/9AejlEZuGenqVcLfURDTPCGB+NHa01UZvcSoKfx+vuHwkAWR3AUZ9VbL+t3wqhgAwpJoKh47aAStSHbaIPBg=='
    }

    def start_requests(self):
        url = 'https://www.linkedin.com/directory/companies/a-1'
        
        cookieFile = 'tutorial/spiders/cookies.json'

        with open(cookieFile) as json_file:
            cookies = json.load(json_file)
            cookies2 = list(map(lambda x: {x['name']:x['value']}, cookies)) 
        
        # yield scrapy.Request(url,headers=self.headers)
        yield scrapy.Request(url,headers=self.headers)

    def parse(self, response):
        print(response.text)

                    


        