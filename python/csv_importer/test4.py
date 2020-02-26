import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
#     'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
#     'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})


# print(df)

# row = df.iloc[1]

# column = df['two']

# df.sub(row, axis='columns')


# df.sub(row, axis=1)


# df.sub(column, axis='index')
# df.sub(column, axis=0)

# dfmi = df.copy()
# dfmi.index = pd.MultiIndex.from_tuples([(1, 'a'), (1, 'b'),
#                                         (1, 'c'), (2, 'a')],
#                                        names=['first', 'second'])
# # print(dfmi)

# dfmi2 = dfmi.sub(column, axis=0, level='second')
# # print(dfmi2)


# data = np.random.randint(0, 7, size=50)

# s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7, 7])

# print(s5.mode())


arr = np.random.randn(20)
factor = pd.cut(arr, 4)
factor = pd.cut(arr, [-5, -1, 0, 1, 5])
print(factor)
