num=int(input("enter the number "))

if(num%2==0):
    print(f"Even Number:{num}")
else:
    print(f"Odd Number:{num}")

#Example 2 — Find the Greatest Number

num1, num2 = map(int, input("Enter two numbers separated by space: ").split())

if num1 > num2:
    print(f"Num1 is greater:{num1}")
else:
    print(f"Num2 is greater :{num2}")