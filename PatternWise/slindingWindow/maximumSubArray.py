'''nums=[1,2]
start=0
window=0
maximum=float('-inf')
k=3
for end in range(len(nums)):
    window+=nums[end]
    if end>=k-1:
        maximum=max(maximum,window)
        window-=nums[start]
        start+=1
    elif k>len(nums):
        maximum=0

print("Maxmimum",maximum)        
'''

def maxSum(nums,k):
    n=len(nums)
    if n<k:
        return 0
    current=sum(nums[:k])
    max_sum=current

    for i in range(k,n):
        current+=nums[i]-nums[i-k]
        max_sum=max(max_sum,current)
    return max_sum
a=[4,8,4,3,2,5,3,2]
print("Maximu sum:",maxSum(a,3),a)

