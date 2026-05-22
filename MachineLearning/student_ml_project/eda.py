import pandas as pd

data=pd.read_csv("student_performance.csv")


# Load data
data = pd.read_csv("student_performance.csv")

# 1. First 5 rows
print("First 5 rows:")
print(data.head())

# 2. Shape (rows, columns)
print("\nShape of data:")
print(data.shape)

# 3. Column names
print("\nColumns:")
print(data.columns)

# 4. Data info
print("\nData Info:")
print(data.info())

# 5. Missing values
print("\nMissing values:")
print(data.isnull().sum())

# 6. Basic statistics
print("\nStatistics:")
print(data.describe())
