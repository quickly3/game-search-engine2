import requests
import random
 
 
url = 'http://baidu.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36icanhazip.com	favicon.ico	'}
 
proxiesLs = [
    '122.138.147.240:9999'
] 

for proxy in proxiesLs:
    proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy,
            }
    try:
        response = requests.get(url,headers = headers,timeout =3,proxies=proxies)
        print(i)
        print(response.text)
    except:
        print('failed')
        pass
