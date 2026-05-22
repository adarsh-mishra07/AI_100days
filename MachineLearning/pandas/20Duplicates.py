import pandas as pd

data={
    'Student':["Adarsh","Adarsh","Amit"],
    'marks':[98,98,34],
    'rank':[1,1,3],
    'Address':["delhi","delhi","Hydrabad"]
}


df=pd.DataFrame(data)
print("Our Dataframe\n",df)

#find duplicate

res=df.duplicated()
print("\n Duplicate:\n",res)

#remove duplicate

res2=df.drop_duplicates()
print("\n Remove Duplicates:\n",res2)
