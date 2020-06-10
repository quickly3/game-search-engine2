import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import codecs

#设置pd的显示长度
pd.set_option('max_colwidth',500)

#载入数据
rows=pd.read_csv('escn.csv', header=0,encoding='utf-8',dtype=str)

segments = []
for index, row in rows.iterrows():
	content = row[10]
	#TextRank 关键词抽取，只获取固定词性
	words = jieba.analyse.textrank(content, topK=50,withWeight=False,allowPOS=('ns', 'n', 'vn', 'v'))
	splitedStr = ''
	for word in words:
		# 记录全局分词
		segments.append({'word':word, 'count':1})
		splitedStr += word + ' '
dfSg = pd.DataFrame(segments)

# 词频统计
dfWord = dfSg.groupby('word')['count'].sum()
#导出csv
dfWord.to_csv('keywords.csv',encoding='utf-8')