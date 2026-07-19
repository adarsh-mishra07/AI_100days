'''
from array import *
a1=array('i',[1,2,3])
print(a1)

for i in range(0,3):
    print(a1[i],end=" ")

a1.append(4)

'''
#duplicate values in array

arr=[1,2,3,2,4,5,1]
length=len(arr)

#by two pointer approach
for i in range(length):
    for j in range(i+1, length):
        if arr[i] == arr[j]:
            print(f"Duplicate found for element: {arr[i]}")