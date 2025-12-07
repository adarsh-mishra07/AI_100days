#Example 1: Print numbers 1 to 5 using recursion
"""
def show(n):
    if n==0:   #base case
      return
    print(n)
    show(n-1)  #recursive call

show(5)

#Example 2: Factorial using recursion

def fact(n):
   if n==0:
      return 1
   return n*fact(n-1)

print(fact(5))


#Example 3: Sum of first N numbers
def sum_n(n):
   if n==0:
      return 1
   return n+sum_n(n-1)

print(sum_n(5))

#Example 4: Fibonacci using recursion
def fib(n):
   if n<=1:
      return n
   return fib(n-1)+fib(n-2)
print(fib(6))


#Example 5: Power (a^b) using recursion

def power(a,b):
   if b==0:
      return 1
   return (a,b-1)
print(power(2,3))

"""
#Example 6: Reverse a string using recursion

def reverseString(s):
   if len(s)==0:
      return ""
   return reverseString(s[1:])+s[0]

print(reverseString("adarsh"))
   