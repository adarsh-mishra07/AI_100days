import pandas as pd

#create a pandas dataframe 


#importing the bost print
from sklearn.datasets import fetch_california_housing
import pandas as pd

california = fetch_california_housing(as_frame=True)
df = california.frame
print(df.head())


#pandas dataframe
california_df=pd.DataFrame(california.data,columns=california.feature_names)