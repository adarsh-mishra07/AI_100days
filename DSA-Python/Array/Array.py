#import array as arr
from array import * 



# How to make array 

val=array('d',[1,2,3,4,5.5])

#print(val)

'''
for i in range(0,5):
    print(val[i], end=" ")

for i in range(0,len(val)):
    print(val[i],end=" \n")

for x in val:
    print(x)

#to know type code 
print(val.typecode)

#to reverse 
val.reverse()

print("\n After reverse")
print(val)


#to insert

val.insert(1,10)
print(val)

#to append 

val.append(100)
print(val)

'''

'''

#copy array 

copyArray= array(val.typecode,( x for x in val))
print("\n I am Copy array")
for i in range(0,len(copyArray)):
    print(copyArray[i],end=" ")
'''




#to delete elements in arrray
'''
copyArray.pop(3)      # 3rd index element deleted 
print("\n Deleted array")
for i in range(0,len(copyArray)):
    print(copyArray[i],end=" ")
    
'''

'''

#slicing 


#a=val[1:4:-1]
#a=val[1:3]
#a=val[::-1]
for i in range(0,len(a)):
  print(a)

'''

'''
#user by input 

ar=array('i',[])
n=int(input("How many number"))
for i in range(0,n):
 ar.append(int(input('enter next numbr')))


for i in range(0,n):
 print("this is all array int nm",ar[i],end=" ")

'''


#searching by index

print(val.index(2))

#-------------------------------------------------------------------------


#if we want to make 2D or 3D array , use the numpy 

#import numpy as np

from numpy import *
'''
arr=array([1,2,5,6,7,8,3,"a",4.5]) # we can make hetrogeneous elements
print()

arr1=array([1,2,3,4.5],float)  #to make float
for i in arr:
    print(i,end=" ")
print()
for i in arr1:
    print(i,end=" ")
'''


#linSpace - to divide in parts

'''
lin=linspace(1,50,5)  # 1 and 50 both included
print(lin)
'''

#arrange  
'''
arran= arange(10,20,3)
print(arran)
'''

#logspace

#if want all element be Zero

'''
ar=zeros(10)
print(ar)

ar1=ones(10)
print(ar1)

ar2=full(10,5)
print(ar2)

'''

# MULTI-DIMENSION

#2-D

twoD= array([[1,3,4,5],[4,2,5,6]])
print(twoD)


# 3-D  - collection of 2D array


threeD = array([
    [[1,2,3],[4,5,6]],   # first 2D array
    [[6,7,8],[9,6,4]]    # second 2D array
])

print(threeD)
print("Shape:", threeD.shape)




