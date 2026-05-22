#Add Labels to a Plot

import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame({
    "cricketBat":["sg","mrf","nike"],
    "mrp":[2000,1000,3000],
    "weight":[1,2,3]

})

plt.plot(df["mrp"],df["weight"])

plt.xlabel("Bat Price (USD)")
plt.ylabel("Bt Weight (Grams)")

plt.show()