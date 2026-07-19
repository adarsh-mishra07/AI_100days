def twoSum(a,target):
 sum=0
 left=0
 right=len(a)-1
 while left<right:
    sum=a[left]+a[right]
    if sum==target:
        print("Pair found in indices:",left,right)
        break
    elif sum<target:
        left+=1
    else:
        right-=1

a=[10,20,30,40,50]
twoSum(a,70)
#time complexity = O(n)
#space complexity = O(1)