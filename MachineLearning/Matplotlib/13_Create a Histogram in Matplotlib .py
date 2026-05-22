#Create a Histogram in Matplotlib 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


arr=np.array([1,2,3])

#histogram 

plt.hist(arr,bins=[0,1,3,4])

plt.xlabel("marks")
plt.ylabel("student")
plt.title("Marksheet")

plt.show()
