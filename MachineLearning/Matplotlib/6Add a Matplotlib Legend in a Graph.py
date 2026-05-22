#Add a Matplotlib Legend in a Graph

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
ax.legend()

plt.title("frequency of figure")

plt.show()