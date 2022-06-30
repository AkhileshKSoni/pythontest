
import pandas as pd

mydata = [
    'BMW', 'AUDI', 'TOYOTA', 'LAMBORGINI'
]

myvar = pd.DataFrame(mydata)

print(myvar)
print("\n")


print("This is the Pandas version : ", pd.__version__)
print("\n")


newSeries = [2, 4, 5, 2, 6, 9]
print(pd.Series(newSeries))
print("\n")




import numpy as np
sers = pd.Series()
print("And the series is : ", sers)

data = np.array(['g', 'e', 'e', 'k', 's'])
print("Array is :", data, end="\n")
print(pd.Series(data))



print("****************************************************************************************************************************")
print("\n")

























