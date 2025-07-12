import pandas as pd

df = pd.read_csv("./Data/data4.csv")
# df = df.fillna({"Date":130})
# new_df = df.dropna(inplace = True)
# df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# print(df.to_string())

print(df.duplicated())