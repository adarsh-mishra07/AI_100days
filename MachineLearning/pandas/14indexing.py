#indexing in csv

import pandas as pd

df =pd.read_csv("C:\\Users\\ADARSH MISHRA\\OneDrive\\Documents\\student.csv" ,index_col="Student")
print("Our Dataframe\n",df)                


#using indexing 
res=df["marks"]
print("\n",res)

#using loc 

res2=df.loc["Adarsh"]
print("\n",res2)

#using iloc

res3=df.iloc[3]
print("\n",res3)