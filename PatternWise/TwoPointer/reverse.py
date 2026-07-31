def reverse(nums):
    left=0
    right=len(nums)-1

    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums

nums=[1,3,4,5,8]
print("Reverse Number:",reverse(nums))

