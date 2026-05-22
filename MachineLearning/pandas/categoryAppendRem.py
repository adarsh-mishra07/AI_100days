import pandas as pd

#addding category
data=['a','b','c','d']

s=pd.Series(data,dtype='category')

print("Series \n",s)

s=s.cat.add_categories('e')
print("\n Update Categories: \n",s)

#remove category 

print("\n remove category :\n")

s=s.cat.remove_categories('d')

print("\n Removed category = d:\n",s)