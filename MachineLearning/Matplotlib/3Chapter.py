#Add Grid Lines to a Plot - grid()

import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame({
    "cricketBat":["sg","mrf","nike"],
    "mrp":[2000,1000,3000],
    "weight":[1,2,3]

})

plt.plot(df["mrp"],df["weight"])

plt.grid()

plt.show()