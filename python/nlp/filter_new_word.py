# encoding=utf-8
import jieba
import re

# jieba.enable_paddle()

def readFileTolist(stopwords_file):
    stopwords = [line.strip() for line in open(stopwords_file,encoding='UTF-8').readlines()]
    return stopwords


words = readFileTolist('./it_cn_words.txt')


for word in words:
    match = re.match(u"[\u4e00-\u9fa5]+", word )
    seg_list = list(jieba.cut(word,use_paddle=True))

    print(seg_list)
    if match:
        print(match)


