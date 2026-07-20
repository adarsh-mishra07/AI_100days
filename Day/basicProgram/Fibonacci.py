def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b
    print("\n")

fib(10)

#if we wnat from some number to some number then we can use while loop
def fib(start, end):

    a, b = 0, 1

    while a <= end:

        if a >= start:
            print(a, end=" ")

        a, b = b, a + b

fib(10, 50)

