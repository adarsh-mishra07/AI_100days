import pandas as pd



dataf=pd.read_csv("C:\\Users\ADARSH MISHRA\\OneDrive\\Documents\\student.csv")
print("\n data :\n",dataf)

#find and replace Null with true

res1=dataf.isnull()
print("\nNew Data Frame: \n",res1.to_string())

#find and replace not Null with true

res2=dataf.notnull()
print("\nNew Data Frame: \n",res2.to_string())

#to drop null value rows s

res3=dataf.dropna()
print("\nDropped Null values:\n",res3)

#find and relace null values with specific value

res4=dataf.fillna(111)
print("\n New df (after replacing new value)\n",res4)