#series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). 
# The axis labels are collectively referred to as the index. 
# A Series is like a fixed-size dictionary in that you can get and set values by index label.
#  It also supports vectorized operations and various methods for data manipulation and analysis.
#it have parameter data,index,dtype,name,copy
#data: to store the data in series
#index: to store the index of the data in series
#dtype: to store the data type of the data in series
#name: to store the name of the series
#copy: to copy the data in series

import pandas as pd

# 1 create a series from a list

data=[10,20,30,40,50]
s1=pd.Series(data)
print("Series:\n",s1)

#another way to create categorical series

s=pd.Series(["p","q","r","s","t"],dtype="category")
print("Categorical Series:\n",s)


#  2  Access a value from the series using index
print("\nAccess a value from the series using index:\n",s1[2])


# 3  Access a value from the series using index label

data=[10,20,30,40,50]
index=['a','b','c','d','e']
s2=pd.Series(data,index=index)
print("\nAccess a value from the series using index label:\n",s2['c'])

# 4  Access a value from the series using index label and index position


data=[10,20,30,40,50]
index=['a','b','c','d','e']
s2=pd.Series(data,index=index)
print("\nAccess a value from the series using index label:\n",s2['c'])
print("\nAccess a value from the series using index position:\n",s2[2])