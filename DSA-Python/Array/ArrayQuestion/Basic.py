#1 Find the maximum and minimum element in an array
"""
n=int(input("enter number of elements"))
arr=[]
for i in range(n):
    num=int=(input(f"enter element{i+1}:"))
    arr.append(num)

maxVal=arr[0]
minVal=arr[0]

for num in arr:
    if num>maxVal:
        maxVal=num
    if num<minVal:
        minVal=num
print("maximum",maxVal)
print("minimum",minVal)
"""



"""
# 2. reverse an array

n=int(input("Enter the element in array"))

arr=[]
for i in range(n):
  num=int(input(f"Enter the element {i+1}:"))
  arr.append(num)

i=0
j=n-1

while i<j:
  arr[i],arr[j]=arr[j],arr[i]  #swap
  i+=1
  j-=1

print("Reverse array:",arr)
"""



#Q3: Second Largest 
"""
n=int(input("Enter the element"))
arr=[]

for i in range(5):
    num=int(input(f"enter element {i+1}:"))
    arr.append(num)

maX=arr[0]
secondMax=float('-inf')
for num in arr:
    if num > maX:
        maX=num

#second largest
for num in arr:
    if num > secondMax and num!=maX:
        secondMax=num

print("Second Largest:",secondMax)
    
"""


#q:4 - even and odd count:
"""
def q4(arr):
    countEven=0
    countOdd=0
    for i in range(len(arr)):
     if arr[i]%2==0:
        countEven+=1
     else:
        countOdd+=1
    
    print("Even:",countEven)
    print("Odd:",countOdd)


num=[1,2,3,4,5,6]
q4(num)

"""

# 5 sum of all elements
"""
n=int(input("array elements:"))
arr=[]
for i in range(n):
    num=int(input(f"Enter the elements {i+1}:"))
    arr.append(num)
sum=0
for num in arr:
  sum+=num
print("sum of all elements:",sum)
"""

#q6 check array is sorted or not 
"""
def is_sorted(arr):
    asc=desc=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            asc=False
        if arr[i]<arr[i+1]:
            desc=False
    return asc or desc
    

arr=list(map(int,input("Enter elements: ").split()))

if is_sorted(arr):
    print("Array is sorted")
else:
    print("array is not sorted")
"""

#q7  remove Duplicate from sorted array
"""

def removeDuplicate(arr):
    if len(arr)==0:
        return []
    j=0

    for i in range(1,len(arr)):
        if arr[i]!=arr[j]:
            j+=1
            arr[j]=arr[i]    
arr=list(map(int,input("Enter elements:").split()))
print("Removed all duplicates:",removeDuplicate(arr))

"""

#q8 move all zero

"""
def moveZero(arr):
 if len(arr)==0:
  return []
 
 j=0
 for i in range(len(arr)):
  if arr[i] !=0:
   arr[j]=arr[i]
   j+=1

#fill remaining with zeros
 for i in range(j,len(arr)):
  arr[i]=0
 return arr


arr=list(map(int,input("Enter elements:").split()))
print("Moved all zero at last:",moveZero(arr))

"""


# 9 finding missing nmbr 

"""
def missingNm(arr):
  n=len(arr)+1

  totalSum=n*(n+1)//2
  arr_sum=0

  for num in arr:
    arr_sum+=num
  
  return totalSum-arr_sum

arr=list(map(int,input("Enter elements:").split()))
print("Missing nmbr:",missingNm(arr))
"""


#10 Find duplicate element
 
 #by set()
"""
def duplicate(arr):
   seen=set()

   for num in arr:
      if num in seen:
         return num
      seen.add(num)

arr=list(map(int,input("Enter elements:").split()))
print("Duplicate nmbr:",duplicate(arr),"\n")
"""
#by sorting 

"""
def duplicate2(arr2):
   arr2.sort()
   for i in range(len(arr2)-1):
      if arr2[i]==arr2[i+1]:
         return arr2[i]

arr2=list(map(int,input("Enter elements:").split()))
print("Duplicate nmbr:",duplicate2(arr2))

"""
#by floyd's cafe

"""
def duplicate3(arr3):
    slow = arr3[0]
    fast = arr3[0]

    while True:
        slow = arr3[slow]
        fast = arr3[arr3[fast]]
        if slow == fast:
            break

    slow = arr3[0]
    while slow != fast:
        slow = arr3[slow]
        fast = arr3[fast]

    return slow

arr3=list(map(int,input("Enter elements:").split()))
print("Duplicate nmbr:",duplicate3(arr3))

"""

# 11 - rotate array by k steps
#input - 1,2,3,4,5,6 , k=3
#output- 5,6,1,2,3,4

"""
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]

def rotateK(arr,k):
    n=len(arr)
    k=k%n

    reverse(arr,0,n-1)   # 6,5,4,3,2,1
    reverse(arr,0,k-1)   # 4,5,6,3,2,1
    reverse(arr,k,n-1)   # 4,5,6,1,2,3


arr=list(map(int,input("Enter the elements").split()))
k=int(input("Enter k"))
print("Rotated Array from k:",rotateK(arr,k))

"""

# 12 Find intersection of two arrays

"""
#if array is sorted , we use two pointer otherwise hash

def intersection(arr1,arr2):
    i=j=0
    result=[]

    while i<len(arr1) and j<len(arr2):
        if arr1[i]==arr2[j]:
            result.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    
    return result

arr1 = list(map(int, input("Enter array1: ").split()))
arr2 = list(map(int, input("Enter array2: ").split()))

print("Intersection:", intersection(arr1, arr2))
"""


# 13 - Find union of two arrays
"""
def union(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1   # FIX

        elif arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])   # FIX
            i += 1

        else:
            if not result or result[-1] != arr2[j]:   # FIX
                result.append(arr2[j])   # FIX
            j += 1

    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not result or result[-1] != arr2[j]:   # FIX
            result.append(arr2[j])   # FIX
        j += 1

    return result


arr1 = list(map(int, input("Enter array1: ").split()))
arr2 = list(map(int, input("Enter array2: ").split()))

print("Union:", union(arr1, arr2))

"""

#14 frequency of each element
"""
Attendance system
Shopping items count
Voting count
"""

"""
def frequency(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


arr = list(map(int, input("Enter elements: ").split()))
result = frequency(arr)

for key, value in result.items():
    print(key, "→", value)

"""

# 15 - Find maximum subarray sum (Kadane’s Algorithm ⭐)
"""
""""Add karo → negative ho gaya → reset karo""""


def maxSuArray(arr):
    max_sum=float('-inf')
    current_sum=0

    for num in arr:
        current_sum+=num

        if current_sum>max_sum:
            max_sum=current_sum

        if current_sum<0:
            current_sum=0
    return max_sum

arr=list(map(int,input("enter elementns:").split()))
print("Maximum subarray sum:",maxSuArray(arr))

"""



# 16.Two Sum problem (target = sum of 2 elements)


   #this approach is hash map
# in this question we have to find the index of two numbers such that they add up to a specific target.
"""
Check karo → mila kya?
Nahi mila → store karo
Mila → return karo

"""

"""
def twoSum(arr,target):
    seen={}
    for i in range(len(arr)):
        num=arr[i]  # current number
        diff=target-num #itne ki jarurat hai target ko achieve karne ke liye
        if diff in seen: #agr diff pehle se seen me hai to iska matlab hai ki humne pehle hi ek number dekha hai jiska sum current number ke sath target ke barabar hai
            return (seen[diff], i) #seen[diff] se hume diff ka index milega aur i se current number ka index milega, dono ko tuple me return kar dete hai
        seen[num] = i  #agr diff nahi mila to current number ko seen me add kar dete hai jisme key num hai aur value i hai, taki future me agar hume diff mile to hum uska index easily access kar sake
    return None  #agr loop ke baad bhi koi pair nahi mila to None return kar dete hai

arr=list(map(int,input("Enter elements:").split()))
target=int(input("Enter target:"))
result=twoSum(arr,target)
if result:
    print("Indices of the two numbers:", result)
else:    print("No two numbers found that add up to the target.")

"""


# two pointer approach 

"""
def twoSum(arr,target):
    i,j=0,len(arr)-1

    while i<j:
     s=arr[i]+arr[j]
     if s==target:
        return (i,j)
     elif s<target:
        i+=1
     else:
        j-=1
     return None

arr=list(map(int,input("Enter elements:").split()))
target=int(input("Enter target:"))  
result=twoSum(arr,target)
if result:
    print("Indices of the two numbers:", result)        

else:
    print("No two numbers found that add up to the target.")
"""


# 17 Sort an array of 0s, 1s, and 2s

def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


arr = list(map(int, input("Enter elements: ").split()))
print("Sorted array:", sort012(arr))