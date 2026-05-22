import pandas as pd


data1={
    'id':['S01','S02','S03'],
    'Student':['Amit','Adarsh','Aadi'],
    'Roll':[90,80,70]
}

data2={
    "id":["S04","S05","S06"],
    'Student':['Rohit','Adha','Yadi'],
    'Roll':[90,80,70]
}

dataFra1= pd.DataFrame(data1,index=["Student1","Student2","Student3"])
print("\nDataframe1:\n",dataFra1)
dataFra2= pd.DataFrame(data2,index=["Student4","Student5","Student6"])
print("\nDataframe2:\n",dataFra2)
Res=pd.concat([dataFra1,dataFra2])
print("\n Concate Data \n",Res)

