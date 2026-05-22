
# how to group data in df and perform operation on it
# we splits the data into groups , then we will iterate through the groups and display the groups

# ex-1= split the object and combine the result
# ex-2 - iterate the group
# ex-3 view the group

# perform aggregation operations on groups

#ex4 - get the mean of the grouped data
# ex-5 - get the size of each group 

# the groupby() method is used in pandas to split the object .
# we can define groupby() as grouping the rows/columns into specific groups


import pandas as pd
import numpy as np

data={
    "player":["virat","rohit","dhni","shikhar"],
    "rank":[1,2,3,4],
    "points":[90,89,76,10],
    "Year":[2012,2022,2024,2025]
}

df=pd.DataFrame(data)

print("\nDataframe:\n",df)



# 1. Group the data on player value

res=df.groupby('player')

#print the first entry
print("\n",res.first())


# 2. Iterate  

for name,group in res:
    print("\n",name)
    print(group)

# 3. View the group
#use the groups property to view the group

print(res.groups)

 # 4. perform Aggregation operations on groups 

# after grouping , we can perform operations on the grouped data using agg() method
# through this method , get the mean or even get the size of each group etc
# get the means of the grouped data 
#  get the size of each group

# to get the mean of the grouped data , first group and then use the agg() method with numpy.mean()

groupRes= df.groupby('Year')

    #use agg() and find mean of points
print("\nMean points per Year:\n", groupRes['points'].agg(np.mean))

# 5. Get the size of each group
print("\nSize of each group:\n", groupRes.size())
