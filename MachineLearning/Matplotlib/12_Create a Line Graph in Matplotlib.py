#Create a Line Graph in Matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

student=np.array(["ashish","rahul","virat"])
marks=np.array([1,2,3])

#line graph

plt.plot(marks,student)

plt.xlabel("marks")
plt.ylabel("student")
plt.title("Marksheet")

plt.show()
