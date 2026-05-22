import pandas as pd
 
# CSV file load karna
data = pd.read_csv("student_performance.csv")

# First 5 rows dikhana
print("Dataset Preview:")
print(data.head())

# Dataset info
print("\nDataset Info:")
print(data.info())
