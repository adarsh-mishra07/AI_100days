import pandas as pd
#to remove whitespace or set of specific characters on text data in as series or dataframe
#by
# 1. strip() , 2.lstrip()  , 3.rstrip()

# 1 - strip() - to remove space from left and right both

data=["\n\tram","shyam\n","\tmohan"]

series=pd.Series(data)

print("\n Series:\n",series)

#remove
print("\n Remove from both the sides:\n",series.str.strip("!\n\t"))


# 2. lstrip()  - to remove from left

print("\n Remove from left sides:\n",series.str.lstrip("!\n\t"))


# 3. rstrip()  - to remove from right

print("\n Remove from right sides:\n",series.str.rstrip("!\n\t"))