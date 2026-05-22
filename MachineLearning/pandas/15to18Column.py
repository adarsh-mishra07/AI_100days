import pandas as pd

df=pd.DataFrame({
    'Student':["Adarsh","Rahul","Amit"],
    'marks':[98,97,34],
    'rank':[1,2,3],
    'Address':["delhi","mumbai","Hydrabad"]
})
print("Our Dataframe\n",df)                

res=df[["marks","rank"]]
print("\n",res)

#data filter

res2= df[df["marks"] > 90]
print("\n",res2)


#select multiple column in a range
print("\n select multiple column in a range \n")
res3=df[df.columns[2:4]]
print("\n",res3)

#insert column

res4=df.insert(3,"Nickname",["Aadi","viru","yas"])
print("\n insert column\n",res4)

print("\n",df)


#assign -

res5=df.assign(Num=[1,2,3])
print("\n Assign column\n",res5)

print("\n",df)

#delete column:

res6=df.drop("marks",axis='columns' )
print("\n DF after removing a column:\n",res6)

#delete row 

res7=df.drop(2,axis='index' )
print("\n DF after removing a row:\n",res7)


#iterating column and rows
print("\n Iterating rows:\n")
for row in df.iterrows():
    print(row)


#iterating rows by itertuples()

print("\n Iterating rows by itertuple:\n")
for row in df.itertuples():
    print(row)


#item() to iterate over columns
print("n Iterate over item()\n")
for a,b in df.items():
 print(a)
 print(b)