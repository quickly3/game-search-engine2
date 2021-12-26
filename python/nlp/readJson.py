# encoding=utf-8
import jieba
import json
import re


articleList_file = '/Users/hongbinzhou/Downloads/article.txt'
f = open(articleList_file,encoding='UTF-8')
wf = open("titles.txt","a")
line = f.readline()

while line:
    article = json.loads(line)
    title = article['_source']['title']

    if title:
        wf.write(title+"\n")

    line = f.readline()

f.close()
wf.close()

