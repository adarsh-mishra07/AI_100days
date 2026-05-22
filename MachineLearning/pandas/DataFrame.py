#Dataframe 

import pandas as pd

data={
    'student':['Amit','Adarsh','jhon'],
    'Rank':[1,2,3],
    'Marks':[90,80,70]
}

#create DF using DataFrame() method with index

df=pd.DataFrame(data,index=['Row A','Row b','Row C'])
print("student Recore\n",df)
print("Datatype:\n",df.dtypes)

# DataFrame ndim attritube  (2)

print("Number of dimension:\n",df.ndim)

#nmbr of element by size attribute  ( 9)

siz=df.size
print("\n Size of Dataframe is:\n",siz)

# 4. shape of DF  (3,3)

Shap= df.shape
print("\n Shape of DataFrame:\n",Shap)

# 5 . index  - Index(['Row A', 'Row b', 'Row C'], dtype='object')
ind= df.index
print("\n Index of DF:",ind)

# 6. Transpose -

print("\n Transpose of our DF:\n",df.T)

# 7. Head 

print("\n Head of our DF:\n",df.head(2))

# 8. Tail

print("\n Tail of our DF:\n",df.tail(2))








