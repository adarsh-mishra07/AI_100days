#Create a Scatter Plot

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


import pandas as pd
import matplotlib.pyplot as plt

#1st ex

team1=[1,2,3,4]
team2=[2,3,4,5]

scorerange=[1,3,4,5]

plt.scatter(team1,scorerange,color='r')
plt.scatter(team2,scorerange,color='b')
plt.xlabel("teamscore")
plt.ylabel("score range")

plt.title("score of two teams")
plt.show()


"""

#2nd ex
data={
    "Temprature":[18,20,33,54,65],
    "Humidity":[23,43,54,12,54],
    "Wind":[10,32,43,53,43],
    "Precipitation":[23,43,54,32,65]
}
df=pd.DataFrame(data,index=["city1","city2","city3","city4","city5"])

df.plot(kind='scatter',x='Temprature',y='Humidity')
plt.show()

"""