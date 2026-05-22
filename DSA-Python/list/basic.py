#1 find max and min in list 
"""
def find_max_min(arr):
    if not arr:
        return None,None
    
    max_val=arr[0]
    min_val=arr[0]

    for i in range(1,len(arr)):
        if arr[i]>max_val:
            max_val=arr[i]
        if arr[i]<min_val:
            min_val=arr[i]
    return max_val,min_val

arr=list(map(int,input("Enter the elements of the list").split()))
max_val,min_val=find_max_min(arr)
print("Maximum:",max_val)
print("Minimum:",min_val)

"""


#2 reverse a string
'''
def rev(s):
    arr=list(s)
    start=0
    end=len(arr)-1
    while start<=end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return ''.join(arr)
s=input("Enter a string")
res=rev(s)
print("Reversed string:",res)

'''

#3 pallindrome string 
'''
def pal(s):
    start=0
    end=len(s)-1
    while start<=end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True
s=input("Enter a string")
res=pal(s)
if res:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

'''

#4 Array sorted
'''
def Sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=list(map(int,input("enter the elements of the list").split()))
res=Sort(arr)
print("Sorted array:",res)

'''

#5 
