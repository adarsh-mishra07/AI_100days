"""
we need to use the plot() method and the Matplotlib library .
The pyplot module from matplotlib is also used for plotting in pandas.
The pyplot.show() is used to display the figure.
"""

"""
install Matplot lib

Ex-1 : Plot a dataframe in pandas
Ex-2 : Histogram
Ex-3 : Pie chart 
Ex-4 : Scatter plot
Ex-5 : Area plot 
"""

import pandas as pd
import matplotlib.pyplot as plt

data={
    "Temprature":[18,20,33,54,65],
    "Humidity":[23,43,54,12,54],
    "Wind":[10,32,43,53,43],
    "Precipitation":[23,43,54,32,65]
}

df=pd.DataFrame(data,index=["city1","city2","city3","city4","city5"])
"""
df.plot()

plt.show()

#------------------------------------------------------------------
#2
#histogram - to show frequency distribution
#-- set the kind argument of the plot() method to hist 
#we need only one column

df["Humidity"].plot(kind='hist')
plt.show()
"""
#------------------------------------------------------------

"""
#3
#Pie chart
#we will create pie chart here , use the plot.pie() method to draw a pie chart

df.plot.pie(y="Humidity")
plt.show()
"""

"""
#4 - scatter plot 
df.plot(kind='scatter',x='Temprature',y='Humidity')
plt.show()
"""

# Area plot
df.plot.area()
plt.show()