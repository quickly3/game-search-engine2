# encoding=utf-8
import jieba
import json
import re

# jieba.enable_paddle()

def stopwordslist():
    stopwords_file = '../../app/Services/stopwords.txt'
    stopwords = [line.strip() for line in open(stopwords_file,encoding='UTF-8').readlines()]
    return stopwords

def ikwordslist():
    stopwords_file = './ik.txt'
    stopwords = [line.strip() for line in open(stopwords_file,encoding='UTF-8').readlines()]
    return stopwords


stopwords = stopwordslist()
ikwords = ikwordslist()
total_word = []

org_word = '每日一博 | 一文搞懂SaaS困境、API经济与Serverless WebAssembly'
seg_list = list(jieba.cut(org_word))

print(seg_list)

# for word in seg_list:
#     if word not in total_word:
#         match = re.match(u"^[\u4e00-\u9fa5]*$", word )
#         if match:
#             print(match.group())
