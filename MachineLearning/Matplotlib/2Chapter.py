#Plot a line with DataFrame 

import matplotlib.pyplot as plt
import pandas as pd

df=pd.DataFrame({
    "cricketBat":["sg","mrf","nike"],
    "mrp":[2000,1000,3000],
    "weight":[1,2,3]

})

plt.plot(df["mrp"],df["weight"])

plt.show()