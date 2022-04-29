# 引入第三方统计包
import pandas as pd
# 读取csv文件
df = pd.read_csv('py_data.csv')

# 数据总数
# count = data.groupby("source").count()
print('批次数量:', df['批次'].nunique())
print('--------------------')
# 按照批次统计
print(df.groupby('批次').size())
print('--------------------')

print('来源种类:', df['来源'].nunique())
print('--------------------')
# 按照来源统计
print(df.groupby('来源').size())
print('--------------------')

print('区县数量:', df['区县'].nunique())
print('--------------------')
# 按照区县统计
print(df.groupby('区县').size())
print('--------------------')

# 按照区县统计是否入场数量
print('按照区县统计是否入场数量')
print(df.groupby(['区县', '是否入场']).size())
print('--------------------')

# 按照区县统计是否完工数量
print('按照区县统计是否完工数量')
print(df.groupby(['区县', '是否完工']).size())
print('--------------------')







