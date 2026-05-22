#single exception
"""
try:
    num=int(input("Enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("O cant divide by zero")
except ValueError:
    print("number is divide by only integer value")

    
    """



#multiple except block

"""
try:
    a=int (input("Enter the f number"))
    b=int (input("enter the s number :"))
    print(a/b)
except(ValueError , ZeroDivisionError):
    print("Error occured")
else:
    print("No error")

"""

#finally block always runs

"""
try:
    even=int(input("enter the even number"))
    if(even%2==0):
       print("even number")
    else:
        print("odd number")
finally:
    print("I am finally")

"""

"""
#custom exception 

age=int(input("Enter your age "))

if age<18:
    raise ValueError("Age must be 18 or above")
else: 
    print("Allowed")

"""


#File Handling + Exception Handling

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File nahi mili")
