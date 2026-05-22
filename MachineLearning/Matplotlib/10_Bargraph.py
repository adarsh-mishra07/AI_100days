#bargraph

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

student=np.array(["ashish","rahul","virat"])
marks=np.array([1,2,3])

#plot graph

plt.bar(student,marks)

plt.xlabel("student")
plt.ylabel("marks")
plt.show()

