#Create a Pie Chart in Matplotlib


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

student=np.array(["ashish","rahul","virat"])
marks=np.array([1,2,3])

#plot graph

plt.pie(marks,labels=student,autopct='%1.2f%%')

plt.title("run score")
plt.show()

