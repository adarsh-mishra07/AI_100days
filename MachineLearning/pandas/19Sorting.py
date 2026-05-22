import pandas as pd

data={
    'Student':["Adarsh","Rahul","Amit"],
    'marks':[98,97,34],
    'rank':[2,1,3],
    'Address':["delhi","mumbai","Hydrabad"]
}
print("Our Dataframe\n",data)

df=pd.DataFrame(data, index=["Row A"," Row B"," Row C"])

print("\n Student Record\n:",df)

#sort

SOrt= df.sort_values(by=['rank'])
print("\n Sort in Ascending:\n",SOrt)



#sort in descending

Des_SOrt= df.sort_values(by=['rank'],ascending=False)
print("\n Sort in Ascending:\n",Des_SOrt)
