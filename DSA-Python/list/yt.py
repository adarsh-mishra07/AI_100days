def first(nums):
    total = 0
    for num in nums:
        total += num
    return total


def second(nums2): 
    new = []
    for num in nums2:
        new.append(num)
    return new


def third(num3):
    l = len(num3)
    matrix = []
    for i in range(l):
        row = []
        for j in range(l):
            row.append(0)
        matrix.append(row)
    return matrix


nums = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 4, 5]
num3 = [1, 2, 3, 4, 5]

print(first(nums))
print("---------")
print(second(nums2))
print("---------")
result = third(num3)
for row in result:
    print(row)
