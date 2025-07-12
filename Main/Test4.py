import pandas as pd 
df = pd.read_csv("./Data/data2.csv")
print(df.to_string())

print(df)
print(pd.options.display.max_rows)
# print(df.loc[[]])
# print(df.head(3))
# print(df.describe())