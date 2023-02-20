import csv
import pprint
import urllib.request as request
import json
import pydash as _
import numpy as np
import pandas as pd
import ssl
import time
from datetime import datetime
import sys

sys.path.append('..')
from es.es_client import EsClient


ssl._create_default_https_context = ssl._create_unverified_context
pp = pprint.PrettyPrinter(indent=4)

def get_stat(mid):
    url = 'https://api.bilibili.com/x/space/upstat?mid={mid}&jsonp=jsonp'
    url = url.replace('{mid}', str(mid))
    header = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'cookie': "buvid3=7CC67FCD-B6E8-36FE-3E43-22EE8B9DD91949990infoc; b_nut=1668480049; i-wanna-go-back=-1; _uuid=F9C10C8310-10418-C10109-6410A-104910A897A13850296infoc; buvid4=1F1FF238-456C-40F1-4F3D-01F04F28E42452129-022111510-NwALtkaT8CZoti6TPA4e2Q%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3916684801054714; nostalgia_conf=-1; b_ut=5; rpdid=|(J|YkYuu)uJ0J'uYY)~~RJYu; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; PVID=2; b_lsid=73A52427_184DD3DCD71; fingerprint=a60c5c54f65db2e93bb35132f207f213; innersign=1; bp_video_offset_23970125=735826012214919200; buvid_fp=7CC67FCD-B6E8-36FE-3E43-22EE8B9DD91949990infoc; SESSDATA=065bb467%2C1685715052%2Cdef8a%2Ac1; bili_jct=ca848c2d435874933ef1d5322cc557cb; DedeUserID=23970125; DedeUserID__ckMd5=d5faf262b47b677a; sid=nc2qr4nw"
    }

    rq = request.Request(url=url, headers=header, method='GET')
    resp = request.urlopen(rq)
    data = json.loads(resp.read())
    return data


def get_follower(mid):
    url = 'https://api.bilibili.com/x/relation/stat?vmid={mid}&jsonp=jsonp'
    url = url.replace('{mid}', str(mid))
    rq = request.Request(url=url, headers=header, method='GET')
    resp = request.urlopen(rq)
    data = json.loads(resp.read())
    return data


def get_cates(mid):
    url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid={mid}&ps=1&tid=0&pn=1&keyword&order=pubdate&order_avoided=true&w_rid=1b65cd1dccf63d0565bf33c8b5384e96&wts=1670319764'
    url = url.replace('{mid}', str(mid))
    rq = request.Request(url=url, headers=header, method='GET')
    resp = request.urlopen(rq)
    data = json.loads(resp.read())
    return data


csv_reader = csv.DictReader(
    open('ups.csv', 'r', encoding='utf-8'), delimiter=',')

output = []

jump = False
jump_to = '24478119'

es = EsClient()

curr_data = 0
for data in csv_reader:
    curr_data+=1
    header = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    mid = data['url'].replace('https://space.bilibili.com/', '')

    if jump:
        # print('Jump Id:', mid)
        if jump_to == mid:
            jump = False
        continue

    url = 'https://api.bilibili.com/x/space/acc/info?mid={mid}&token=&platform=web&jsonp=jsonp'
    url = url.replace('{mid}', str(mid))

    print(url, curr_data, 1267)
    rq = request.Request(url=url, headers=header, method='GET')
    resp = request.urlopen(rq)
    info = json.loads(resp.read())

    up = {}
    up['id'] = mid
    up['space'] = data['url']
    up['name'] = _.get(info, 'data.name')
    up['sex'] = _.get(info, 'data.sex')
    up['face'] = _.get(info, 'data.face')
    up['sign'] = _.get(info, 'data.sign')
    up['rank'] = _.get(info, 'data.rank')
    up['level'] = _.get(info, 'data.level')
    up['birthday'] = _.get(info, 'data.birthday')
    up['school'] = _.get(info, 'data.school.name')
    up['profession'] = _.get(info, 'data.profession.name')

    up['tags'] = _.get(info, 'data.tags')

    up['offical_title'] = _.get(info, 'data.official.title')
    up['offical_desc'] = _.get(info, 'data.official.desc')
    up['nameplate'] = _.get(info, 'data.nameplate.name')

    fdata = get_follower(mid)
    up['follower'] = _.get(fdata, 'data.follower')
    up['following'] = _.get(fdata, 'data.following')

    sdata = get_stat(mid)
    up['archive'] = _.get(sdata, 'data.archive.view')
    up['likes'] = _.get(sdata, 'data.likes')

    cdate = get_cates(mid)

    cates = _.get(cdate, 'data.list.tlist')
    total = _.get(cdate, 'data.page.count')
    lastCreated = _.get(cdate, 'data.list.vlist[0].created')

    cates_list = []
    if cates:
        for key in cates:
            cates_list.append(cates[key])

        cates_list = sorted(cates_list, key=lambda d: d['count'])
        cates_list.reverse()

        most_cate = max(cates_list, key=lambda x: x['count'])

        cates_list = list(
            map(lambda x: x['name']+':'+str(x['count']), cates_list))
        cates_list =  " | ".join(cates_list)

    up['total'] = total

    up['last_created'] = ''
    if lastCreated:
        up['last_created'] = datetime.fromtimestamp(lastCreated)

    up['cates'] = cates_list

    if most_cate:
        up['most_cate'] = most_cate['name']

    bulk = []
    doc = {}

    doc['user_id'] = up['id']
    doc['user_name'] = up['name']
    doc['avatar_large'] = up['face']
    doc['description'] = up['offical_desc']
    doc['blog_address'] = up['space']
    doc['post_article_count'] = up['total']
    doc['digg_article_count'] = up['likes']
    doc['view_article_count'] = up['archive']
    if up['offical_title']:
        doc['titles'] = up['offical_title'].split("、")
    doc['sign'] = up['sign']

    doc['follower_count'] = up['follower']
    doc['followee_count'] = up['following']

    doc['nameplate'] = up['nameplate']
    doc['source'] = 'bilibili'

    bulk.append(
        {"index": {"_index": "author"}})
    bulk.append(doc)

    if len(bulk) > 0:
        resp = es.client.bulk(body=bulk)

    output.append(up)
    time.sleep(1)
    dfSg = pd.DataFrame([up])
    dfSg.to_csv('ups_detail.csv', mode='a',
                encoding='utf-8', index=False, header=False)
