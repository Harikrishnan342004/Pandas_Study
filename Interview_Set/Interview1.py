import pandas as pd
df = pd.read_csv("C:/Users/HARI KRISHNAN/Desktop/Pandas_Study/Data/Data5.csv")
duplicates = df[df.duplicated(keep=False)]

print(duplicates)