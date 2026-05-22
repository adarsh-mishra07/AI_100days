"""
we will work around statistics operations using the statistical functions in python pandas 
it can be applied to a pandas series or dataframe 

"""
import pandas as pd
data={
   "math":[ 10,20,30,50],
   "science":[2,3,4,5],
   "sst":[10,34,25,33],
   
}
df=pd.DataFrame(data)
print("Dataframe\n",df)


#1. sum()
print("\nSum\n",df.sum())

# 2.count() - count of non-empty value

print("\n Count \n",df.count())

# 3. max()

print("\n Count\n",df.max())

# 4. min()
print("\nMin:\n",df.min())

# 5. mean()
print("\nMean\n",df.mean())

# 6. median
print("\nMeadian\n",df.median)

#7. mode
print("\nmode\n",df.mode())

# 8 . std()

print("\nStd:\n",df.std())

#9 describe()

print("\nDescribe:\n",df.describe())