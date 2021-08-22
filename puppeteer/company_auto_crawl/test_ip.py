import requests

proxies = {
           'https': '179.1.84.122:999',
           'http': '67.207.83.225:80'
        }
url = "https://www.baidu.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
try:
    response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    print(response.text)
except Exception as e:
    print(f"请求失败，代理IP无效！")
    print(e)
else:
    print("请求成功，代理IP有效！")