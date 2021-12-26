# encoding=utf-8
import jieba
import json
import re

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


filename = 'titles.txt'
current = 0
print("开始进行分词")

count = len(open(filename,'r').readlines())


with open(filename,'r') as f:
    for line in f.readlines():
        linestr = line.strip()
        # data = json.loads(linestr)
        seg_list = list(jieba.cut(linestr))

        # ret = [ i for i in seg_list if i not in stopwords ]

        current+=1
        if current%1000 == 0:
            print("{}/{}".format(current,count))

        seg_list =  list(set(seg_list))
        for word in seg_list:
            match = re.match(u"^[\u4e00-\u9fa5]*$", word )
            if match:
                total_word.append(word)

total_word =  list(set(total_word))

print("过滤停用词")
ret = [ i for i in total_word if i not in stopwords ]
print("过滤IK分词器已有词典")
ret2 = [ i for i in ret if i not in ikwords ]

ret2.sort()

with open ("it_cn_words.txt", "w") as thefile:
    thefile.write("\n".join(ret2))