# encoding=utf-8

def readFileTolist(stopwords_file):
    stopwords = [line.strip() for line in open(stopwords_file,encoding='UTF-8').readlines()]
    return stopwords


cn_words = readFileTolist('./cn_dict.txt')
ik_words = readFileTolist('./ik.txt')


ret = [ i for i in cn_words if i not in ik_words ]

ret.sort()

with open ("cn_words2.txt", "w") as thefile:
    thefile.write("\n".join(ret))
