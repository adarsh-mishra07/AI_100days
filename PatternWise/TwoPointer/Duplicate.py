def RemDuplicate(nums):
    if not nums:
        return 0
    left=0
    n=len(nums)
    right=left+1
    while right<n:
        if nums[left]==nums[right]:
            right+=1
        else:
            nums[left+1]=nums[right]
            left+=1
    return left+1

nums = [2,2,3,4]
b=[]
print(RemDuplicate(nums), nums)