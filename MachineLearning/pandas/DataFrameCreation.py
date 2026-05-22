import pandas as pd


# 1.  Create a Pandas DataFrame
#dataset

"""

data={
    'Student':['Adarsh','Mishra','Shivam','Mishra'],
    'Rank':['Caption','Ins','Caption','Ins'],
    'Marks':[90,50,60,78]
}

df=pd.DataFrame(data)

print("Student Records\n",df)

"""

#  2.  Access a group of rows or columns in a Pandas DataFrame

data={
    'Student':['Adarsh','Mishra','Shivam','Mishra'],
    'Rank':['Caption','Ins','Caption','Ins'],
    'Marks':[90,50,60,78]
}

df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD'])

print("Student record\n",df)

#access the value in the student corresponding RowA label
print("Value=",df.loc['RowA','Student'])



#----------------------------------------------------
# 3.Access a group of rows or columns by integer positions in a Pandas DataFrame
#---------------------------------------------------------
# dataframe.iloc is used to access a group of rows or column by integers .
# we have also set columns and indexes

'''
data={
    'Student':['Adarsh','Mishra','Shivam','Mishra'],
    'Rank':['Caption','Ins','Caption','Ins'],
    'Marks':[90,50,60,78]
}

df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD'])

print("Student record\n",df)
print("value=\n",df.iloc[[1,2]])

'''



# 4  Name your own indexes in a Pandas DataFrame

#the index argument is used to set and name your own indexes in a dataframe 

'''
data={
    'Student':['Adarsh','Mishra','Shivam','Mishra'],
    'Rank':['Caption','Ins','Caption','Ins'],
    'Marks':[90,50,60,78]
}

df=pd.DataFrame(data,index=['Student1','Student2','Student3','Student4'])
print("Student Records\n\n",df)


'''

# 5 Iterating a DataFrame


data={
    'Student':['Adarsh','Mishra','Shivam','Mishra'],
    'Rank':['Caption','Ins','Caption','Ins'],
    'Marks':[90,50,60,78]
}

df=pd.DataFrame(data,index=['Student1','Student2','Student3','Student4'])
print("Student Records\n\n",df)

for col in df:
    print(col)
