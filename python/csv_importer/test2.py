import csv
import os
import numpy as np
import pandas as pd
from elasticsearch import Elasticsearch

# tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
#                      'foo', 'foo', 'qux', 'qux'],
#                     ['one', 'two', 'one', 'two',
#                      'one', 'two', 'one', 'two']]))

# print(tuples)

# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

# print(index)

# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

# print(df)
# df2 = df[:4]
# print(df2)

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": [
                  'a', 'b', 'b', 'a', 'a', 'e']})

df["grade"] = df["raw_grade"].astype("category")

print(df["grade"].cat.categories)

df["grade"].cat.categories = ["very good", "good", "very bad"]


df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"])
# df['raw_grade'].iloc[0] = "b"
# print(df)

print(df.groupby("grade").size())
