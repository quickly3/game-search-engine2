import pandas as pd
file = "../numpy/escn.csv"
df = pd.read_csv(file,delimiter=",")


# df = df.drop(["_id","_index","_score","_type","stars","tag","source"], axis=1)
# df = df.drop(["Unnamed: 0"], axis=1)

# df['title'] = df['title'].str.strip(" ")
# df['summary'] = df['summary'].str.strip(" ")


# df.to_csv(file,quoting=1,index=False)


# df2 = df[df<2020]

# print(df.column.dtype)
# print(df.dtypes)

df2 = df.copy()

# where update
# df2 = df2[df2['created_year'] == 2020]

df3 = df2.query("created_year>2019")

print(df3.loc[0])
