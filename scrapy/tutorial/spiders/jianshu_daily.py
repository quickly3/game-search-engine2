# -*- coding:UTF-8 -*-
#
#

import scrapy
import json
from string import Template
import random

class AliSpider(scrapy.Spider):
    # 593
    name = "jianshu_daily"

    domain = 'https://www.jianshu.com'

    c = [
        "python","javascript","php","css",
        "typescript","node","linux","postgresql",
        "security","game","blockchain"
    ]

    url_model = Template(
        "https://www.jianshu.com/search/do?q=${q}&type=note&page=${page}&order_by=published_at")

    page = 1

    def start_requests(self):

        q = "python"
        version = 530+random.randint(0, 9)
        refer_model = Template(
            "https://www.jianshu.com/search/do?q=${q}&type=note&page=${page}&order_by=published_at")

        user_agent_model = Template(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/${version}.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/${version}.36")

        url = self.url_model.substitute(q=q, page=self.page)
        referer = refer_model.substitute(q=q, page=self.page)
        user_agent = user_agent_model.substitute(version=version)

        jianshu_headers = {
            "authority": "www.jianshu.com",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "accept": "application/json",
            "origin": "https://www.jianshu.com",
            "user-agent": user_agent,
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": referer,
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
            "x-csrf-token:":"wYFhf2K8TKihNHPvSfMOef6E3et92hnwCrfztMDWYLQdjl60B+kQUOTQusvVSxWTqRLTUgSTimQbcdgpunm+Ng==",
            "cookie":"__gads=ID=e1520e2b3b529fff:T=1581320484:S=ALNI_MZezyEzlwwlQffbTqzYtfpp3SBJ_w; _ga=GA1.2.1641834497.1582042807; read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1607942094; __yadk_uid=LGdtkXn3kbd7jy4ppVyHm2HOWFMCWjGT; web_login_version=MTYwNzk0MjIzMA%3D%3D--3e0dfcd565ce1017a793160834db0003a6c28b16; _gid=GA1.2.1939802003.1607942319; _m7e_session_core=461029a5978273bc4fbe440b89eb9dc5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e5917137a383-047b243bb040d9-1d3a6a5a-2073600-16e5917137b138%22%2C%22%24device_id%22%3A%2216e5917137a383-047b243bb040d9-1d3a6a5a-2073600-16e5917137b138%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22search-recent%22%2C%22%24latest_utm_campaign%22%3A%22maleskine%22%2C%22%24latest_utm_content%22%3A%22note%22%7D%2C%22first_id%22%3A%22%22%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3Dpython%26utm_source%3Ddesktop%26utm_medium%3Dsearch-recent; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1607950071"
        }

        yield scrapy.Request(url, headers=jianshu_headers, method='POST')

    def parse(self, response):

        rs = json.loads(response.text)
        print(rs)
