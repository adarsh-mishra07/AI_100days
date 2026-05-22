#Position Matplotlib Legends
#we ca set abovethese 9 values
"""
upper left ,upper right ,lower left , lower right
upper centre ,lower center , center left ,center right
center
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

a=np.arange(5)
b=[2,4,6,8,10]
c=[5,6,8,9,10]

#create plots
fig=plt.figure()
ax=plt.subplot()

ax.plot(a,b,'k--',label='frequency')
ax.plot(a,c,'k:',label='periods')

#create legend
ax.legend(loc="upper center")

plt.title("frequency of signal")

plt.show()