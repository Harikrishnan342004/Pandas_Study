import pandas as pd 

mydataset = {
    'cars': ["BMW" , "Volvo" , "Ford"],
    'passing': [3,7,2]
}
type(mydataset)
var = pd.DataFrame(mydataset)
print(var)