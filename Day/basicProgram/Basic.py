
#check prime number

import math
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

a=is_prime(29)
print(a)


#fibonacci series

def print_fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b

print_fibonacci(10)
