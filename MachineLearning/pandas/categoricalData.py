#it is pandas categorical data type
#it is used to store the categorical data in pandas
#Categorical data is a type of data that can take on a limited, fixed number of possible values.
#Categorical data is often used to represent qualitative data, such as gender, color, or categories.

#  1 -->  create categorical series 

import pandas as pd

data=['red','blue','green','red','blue']
cat_series=pd.Series(data,dtype='category')

print("Categorical Series:\n",cat_series)


#another way to create categorical series

s=pd.Series(["p","q","r","s","t"],dtype="category")
print("Categorical Series:\n",s)


#  2 --->   creating categorical dataframe
df=pd.DataFrame({"cat1":['red','blue','green','red','blue'],
                 "cat2":['small','medium','large','small','medium'],
                 "cat3":['A','B','C','D','E'],
                 "shape":['circle','square','triangle','circle','square']})
print("Categorical DataFrame:\n",df)


