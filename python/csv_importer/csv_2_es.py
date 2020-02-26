import csv
import os
import numpy as np
import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch()
index = "app_test4"
count = 0
max = 1000
# filePath = 'F:\download\ciq_industry.csv'

# df = pd.read_csv(filePath)
# print(df.head(10))

dates = pd.date_range("2020-02-20", periods=6)
# print(data_df)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# print(df[df.childlevel == 3])

# print(df.sort_index(axis=1))


# print(dates[0])
# print(df.loc[dates[0]])

# print(df.iloc[:5, 0:2])

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

# print(df2)

res = df2[df2['E'].isin(['one', 'two'])]

s1 = pd.Series([1, 2, 3, 4, 5, 6],
               index=pd.date_range('2020-02-20', periods=6))
# print(res)
df['F'] = s1
df.at[dates[0], 'A'] = 0
df.iat[0, 1] = 2
df.loc[:, 'D'] = np.array([9] * len(df))
# df.D = 6
# print(df)
# print([5] * 4)

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1

df1.dropna(how='any')
res = df1.fillna(value=5)

# print(df1)
# print(res)

# print(df)
# print(df.mean())
# print(df.mean(1))

# s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
# print(df)

# ss = df.sub(s, axis='index')
# print(ss)


s = pd.Series(np.random.randint(0, 7, size=10))
print(s.value_counts())
