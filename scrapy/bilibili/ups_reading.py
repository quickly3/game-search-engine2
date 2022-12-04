import csv
import pprint
import urllib.request as request;
import json
import pydash as _
import numpy as np
import pandas as pd


pp = pprint.PrettyPrinter(indent=4)

def get_stat(mid):
    url = 'https://api.bilibili.com/x/space/upstat?mid={mid}&jsonp=jsonp'
    url = url.replace('{mid}',str(mid))
    header = {
        'Accept':'application/json, text/plain, */*',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'cookie':"buvid3=7CC67FCD-B6E8-36FE-3E43-22EE8B9DD91949990infoc; b_nut=1668480049; i-wanna-go-back=-1; _uuid=F9C10C8310-10418-C10109-6410A-104910A897A13850296infoc; buvid4=1F1FF238-456C-40F1-4F3D-01F04F28E42452129-022111510-NwALtkaT8CZoti6TPA4e2Q%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3916684801054714; nostalgia_conf=-1; b_ut=5; rpdid=|(J|YkYuu)uJ0J'uYY)~~RJYu; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; PVID=2; b_lsid=73A52427_184DD3DCD71; fingerprint=a60c5c54f65db2e93bb35132f207f213; innersign=1; bp_video_offset_23970125=735826012214919200; buvid_fp=7CC67FCD-B6E8-36FE-3E43-22EE8B9DD91949990infoc; SESSDATA=065bb467%2C1685715052%2Cdef8a%2Ac1; bili_jct=ca848c2d435874933ef1d5322cc557cb; DedeUserID=23970125; DedeUserID__ckMd5=d5faf262b47b677a; sid=nc2qr4nw"
    }

    rq = request.Request(url=url,headers=header,method='GET')
    resp = request.urlopen(rq)
    data = json.loads(resp.read())
    return data


def get_follower(mid):
    url = 'https://api.bilibili.com/x/relation/stat?vmid={mid}&jsonp=jsonp'
    url = url.replace('{mid}',str(mid))
    rq = request.Request(url=url,headers=header,method='GET')
    resp = request.urlopen(rq)
    data = json.loads(resp.read())
    return data


csv_reader = csv.DictReader(open('ups.csv', 'r', encoding='utf-8'), delimiter=',')

output = []
for data in csv_reader:
    pp.pprint(data)
    header = {
        'Accept':'*/*',
        'User-Agent':'Thunder Client (https://www.thunderclient.com)'
    }
    mid = data['url'].replace('https://space.bilibili.com/','')
    url = 'https://api.bilibili.com/x/space/acc/info?mid={mid}&token=&platform=web&jsonp=jsonp'
    url = url.replace('{mid}',str(mid))

    print(url)
    rq = request.Request(url=url,headers=header,method='GET')
    resp = request.urlopen(rq)
    info = json.loads(resp.read())

    up = {}
    up['space'] = data['url']
    up['name'] = _.get(info,'data.name')
    up['sex'] = _.get(info,'data.sex')
    up['face'] = _.get(info,'data.face')
    up['sign'] = _.get(info,'data.sign')
    up['rank'] = _.get(info,'data.rank')
    up['level'] = _.get(info,'data.level')
    up['birthday'] = _.get(info,'data.birthday')
    up['school'] = _.get(info,'data.school.name')
    up['profession'] = _.get(info,'data.profession.name')

    up['tags'] = _.get(info,'data.tags')

    up['offical_title'] = _.get(info,'data.official.title')
    up['offical_desc'] = _.get(info,'data.official.desc')
    up['nameplate'] = _.get(info,'data.nameplate.name')

    fdata = get_follower(mid)
    up['follower'] = _.get(fdata,'data.follower')
    up['following'] = _.get(fdata,'data.following')

    sdata = get_stat(mid)
    up['archive'] = _.get(sdata,'data.archive.view')
    up['likes'] = _.get(sdata,'data.likes')

    pp.pprint(up)
    output.append(up)

    break;

dfSg = pd.DataFrame(output)
dfWord = dfSg.groupby('word')['count'].sum()
dfWord.to_csv('keywords.csv',encoding='utf-8')