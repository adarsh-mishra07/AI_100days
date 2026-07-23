def SON(*number):
    total = 0
    for num in number:
        total += num
    return total

n = [10, 20, 30]
print(SON(*n))
