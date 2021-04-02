import requests
import random
 
 
url = 'http://searchgank.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36icanhazip.com	favicon.ico	'}
 
proxiesLs = [
    '189.113.217.35:49733'
] 

for proxy in proxiesLs:
    proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy,
            }
    try:
        response = requests.get(url,headers = headers,timeout =3,proxies=proxies)
        print(proxy)
        print(response.text)
    except:
        print('failed')
        pass
