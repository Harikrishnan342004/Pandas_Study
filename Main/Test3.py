import pandas as pd

a = ["hari" , "Kavi" , "Meena"]
# a = [1, 7, 2]
myvar = pd.Series(a)
myvar2 = pd.Series(a, index=["x" , "y" , "z"])
print(myvar[2])
print(myvar2)