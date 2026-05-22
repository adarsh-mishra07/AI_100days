import pandas as pd

data1={
    'id':['S01','S02','S03'],
    'Student':['Amit','Adarsh','Aadi'],
    'Roll':[90,80,70]
}

data2={
    'Rank':[1,2,3],
    'MArks':[90,80,70]
}

#Adding Dataset in Dataframe

dataFrame1= pd.DataFrame(data1)
print("DataFrame1:\n",dataFrame1)
dataFrame2=pd.DataFrame(data2)
print("DataFrame2:\n",dataFrame2)

#join two Dataframe 

resDf= dataFrame1.join(dataFrame2)
print("\n join Dataframe:\n",resDf)


