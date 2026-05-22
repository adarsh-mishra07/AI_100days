import pandas as pd
import numpy as np
data=[np.nan,"ABC","ADARSH Mishra","rahul",np.nan]

#SERIES
series=pd.Series(data)
print("\n Series:\n",series)

#convert in lower

print("\nLower case\n",series.str.lower())

#convert in upper

print("\nupper case\n",series.str.upper())

#convert in came case by title method

print("\Camel case\n",series.str.title()) 

#find length of each elements

print("\Length case\n",series.str.len())

#to count non-empty cells

print("\nCount of non-empty\n",series.count())

# contains() - to search for a value in a column

print("\nContains values\n",series.str.contains("ADARSH Mishra"))