import pandas as pd

# 读取第一个CSV文件并创建数据框
df = pd.read_csv('authors1.csv')

# 依次读取其他CSV文件，并将它们追加到数据框中
files = ['authors2.csv', 'authors3.csv']  # 替换为您实际的文件名列表
for file in files:
    temp_df = pd.read_csv(file)
    df = df.append(temp_df)

# 去除重复项
df = df.drop_duplicates()
df = df.sort_values('id')

# 将合并后的数据保存到新的CSV文件中
df.to_csv('authors_merged.csv', index=False)
