
import numpy as np
"""This script demonstrates the performance difference between Python lists and NumPy arrays."""
"""
from time import process_time as pt

python_list=[i for i in range(1000000000)]
start_time=pt()
python_list=[i+5 for i in python_list]
end_time=pt()
print("Python list processing time:", end_time - start_time)
"""

"""
np_array=np.array([i for i in range(1000000000)])
start_time=pt()
np_array=np_array+5
end_time=pt()
print("NumPy array processing time:", end_time - start_time)

"""

"""
# Example of numpy array creation and basic operations

np_array=np.array([1,2,3,4,5])
print("Numpy Array:",np_array)
print(np_array.shape)

np_array2=np.array([[1,2,3],[4,5,6]])
print("Numpy 2D Array :\n",np_array2)
print("Shape of 2D Array :",np_array2.shape)

np_array3=np.array([[1,2,3],[4,5,6]],dtype=float)
print("Numpy 2D Array :\n",np_array3)
print("Shape of 2D Array :",np_array3.shape)

"""

"""
#initial placeholders in numpy arrays

#creating an array of zeros
zeros_array=np.zeros((3,4))
print("Array of zeros:\n",zeros_array)

#creating an array of ones
ones_array=np.ones((3,4))
print("Array of ones:\n",ones_array)

#creating an array ,All the value are initialized to a specific value
specific_array=np.full((3,4),5)
print("Array of ones:\n",specific_array)

"""


"""
#create an identity matrix 
a=np.eye(5)
print(a)
"""
"""
#create a numpy array with random value
b=np.random.random((3,4))
print(b)
print("Shape of arry:",b.shape)

"""

"""
#randint
rint=np.random.randint(1,10,(3,4))
print(rint)
print("Shape of arry:",rint.shape)
"""

"""
#array of evenly space value   - spepcifying the nmbr of value required
d=np.linspace(1,50,10)
print(d)
"""

"""
#array of evenly spece value - specify the step size
e=np.arange(1,50,5)
print(e)
"""

"""
#conver the list to numpy array  
my_list=[1,2,3,4,5]
my_array=np.asarray(my_list)
print("List to numpy array:",my_array)
print("Type:",type(my_array))
"""

"""
#analysis of numpy array
c=np.random.randint(1,100,(4,5))
print("Array:\n",c)
print("Shape of array:",c.shape)

#array dimentsion
print("Dimention of array:",c.ndim)

#total nmbr element in array
print("TOtal nmbr elements in arrya",c.size)


#data type of array elemetns 

print(c.dtype)

"""



'''
#mathematical operation on numpy array 
A1=np.random.randint(1,10,(5))
A2=np.random.randint(1,10,(5))
print("Array 1:",A1)
print("Array 2:",A2)
print("Addition:",A1+A2)
print("Substraction:",A1-A2)
print("Multiplication:",A1*A2)
print("Division:",A1/A2)
print("Expo:",A1**A2)
'''
'''
#add fun
a1=np.random.randint(1,10,(3,3))
a2=np.random.randint(1,10,(3,3))
print("Array 1:",a1)
print("Array 2:",a2)
print("Additio using np.add():\n",np.add(a1,a2))
#same as subs
print("Substraction using np.sub():\n",np.subtract(a1,a2))
#same as mult
print("Multiplication using np.mul():\n",np.multiply(a1,a2))
#same as div
print("Division using np.div():\n",np.divide(a1,a2))
#same as expo
print("Expo using np.exp():\n",np.exp(a1))
'''
'''
#Array MAnipulation
array= np.random.randint(1,20,(2,3))
print(array)
print("Shape of array:",array.shape)

#tranpose - ways to make rows as column and column as rows
trans=np.transpose(array)
print("Transposed array:\n",trans)
print("Shape of transposed array:",trans.shape)

#another way to transpose 
trans2=array.T
print(trans2)
print(trans2.shape)
'''

#reshaping the array - use to change the shape of array where total nmbr of element remain same but shape change
array2= np.random.randint(1,20,(2,3))
print(array2)
print("Shape of array:",array2.shape)

reshaed=array2.reshape(3,2)
print("Reshaped array:\n",reshaed)
print("Shape of reshaped array:",reshaed.shape)