import pandas as pa

reading_variable = pa.read_csv('Data/data.csv')
print(reading_variable.to_string())

print(pa.__version__ )  