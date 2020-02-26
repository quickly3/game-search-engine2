import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])

# print(s.array)
# print(s.index.array)

# print(s.to_numpy())
# print(np.asarray(s))

ser = pd.Series(pd.date_range('2000', periods=2, tz="CET"))

ser.to_numpy(dtype=object)

print(ser)
