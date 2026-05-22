#Series Attribute methods are used to access the attributes of a Series object in pandas.
# Some of the commonly used Series Attribute methods are:
# 1. index: This attribute returns the index of the Series. It is an immutable array-like object that labels the elements of the Series.
# 2. values: This attribute returns the values of the Series as a NumPy array
# 3. dtype: This attribute returns the data type of the values in the Series.
# 4. name: This attribute returns the name of the Series.
# 5. size: This attribute returns the number of elements in the Series.
# 6. shape: This attribute returns the shape of the Series as a tuple (number of elements,).
# 7. ndim: This attribute returns the number of dimensions of the Series, which is always 1 for a Series.
# 8. empty: This attribute returns True if the Series is empty (i.e., has no elements), and False otherwise.
# 9. T: This attribute returns the transpose of the Series, which is the same as the original Series since it is one-dimensional.
# 10 hasnans: This attribute returns True if the Series contains any NaN (Not a Number) values, and False otherwise.
# 11 head(n): This method returns the first n elements of the Series. If n is not specified, it returns the first 5 elements by default.
# 12 tail(n): This method returns the last n elements of the Series. If n is not
# 13 info(): This method provides a concise summary of the Series, including the number of non-null values, data type, and memory usage.
# 14 describe(): This method generates descriptive statistics of the Series, such as count, mean, standard deviation, minimum, and maximum values.

import pandas as pd

# 1.  create a series from a list and access the attributes of the series
data=[10,20,30,40,50]
d=pd.Series(data)

print("Index of the series:", d.index)
print("Values of the series:", d.values)
print("Data type of the series:", d.dtype)
print("Name of the series:", d.name)
# 2. to make name 
data=[10,20,30,40,50]
d=pd.Series(data , name="MySeries")
print("Name of the Series:", d.name)
print("Size of the series:", d.size)
print("Shape of the series:", d.shape)
print("Number of dimensions of the series:", d.ndim)
print("Is the series empty?", d.empty)
print("Transpose of the series:", d.T)
print("Does the series have any NaN values?", d.hasnans)
print("Head of series :\n", d.head(3))
print("Tail of series :\n", d.tail(3))
print("Info of series :\n", d.info())