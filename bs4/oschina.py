# from bs4 import BeautifulSoup
import requests
url = "https://www.oschina.net/search?scope=blog&q=python&onlyme=0&onlytitle=0&sort_by_time=1&p=3"

headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "www.oschina.net",
    "Pragma": "no-cache",
    "Referer": "https://www.oschina.net/search?scope=blog&q=python&onlyme=0&onlytitle=0&sort_by_time=1&p=2",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "X-PJAX": "true",
    "X-PJAX-Container": ".search-container",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "_ga=GA1.2.186448612.1576823180; __gads=ID=9759499603a966d2:T=1587006988:S=ALNI_MaHUCvHBDV4_9p3hvYSCpQ0OHpY1A; _user_behavior_=7c8e975a-2707-44d8-93af-28d6d29010d4; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1610426992; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1610965672"
}

proxy = {
    "https":"58.220.95.35:10174"
}

r = requests.get(url,headers=headers,proxies=proxy)


print(r.status_code)


# soup = BeautifulSoup(html)