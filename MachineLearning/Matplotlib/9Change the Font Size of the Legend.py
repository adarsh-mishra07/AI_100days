#change the font size of legend
"""
xx-small , x-small , small , medium,large,x-large,xx-large

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
legend=ax.legend(loc="upper center",fontsize='medium')

#set background
legend.get_frame().set_facecolor('red')

#plot title
plt.title("frequency of signal")

plt.show()