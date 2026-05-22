#combine the two series into one
#it uses in data analysis and data manipulation


import pandas as pd

"""
# This was the old way to combine two series into one

data=[10,20,30,40,50]
index=['a','b','c','d','e']
s1=pd.Series(data,index=index)
data2=[60,70,80,90,100]
s2=pd.Series(data2,index=index)
#combine the two series into one
combined_series=s1+s2
print("Combined Series:")
print(combined_series)

"""

# We want greater value from two series 

data1=[10,20,30,40,50]
data2=[60,70,80,90,100]
print("Series 1:\n",data1)
print("Series 2:\n",data2)
s1=pd.Series(data1)
s2=pd.Series(data2)

def Great(x,y):
    if x>y:
        return x
    else:
        return y
GreateValue=s1.combine(s2,Great)  # Great function is passing as a parameter in combine method to compare the values of two series and return the greater value
print("Greater Value from two series:\n",GreateValue)

