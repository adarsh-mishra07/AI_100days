#brute force approach
"""def threeSum(nums, target=0):
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 2):
        # skip duplicate 'first' values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicates for left and right
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1

    return res


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4], 0))
"""
#optimized approach by sorting and using two pointer technique

def solution2(arr,target):
    arr.sort()
    n=len(arr)
    res=set()
    i=0
    j=n-2
    k=n-1
    while i<j<k:
        if arr[i]+arr[j]+arr[k]==target:
            triplet=tuple(sorted([arr[i],arr[j],arr[k]]))
            res.add(triplet)
            j+=1
            k-=1
        elif arr[i]+arr[j]+arr[k]<target:
            j+=1
        else:
            k-=1
    return [list(t) for t in res]
print(solution2([-1,0,1,2,-1,-4],1))