#Concepts to Learn - Day 2: Conditional Statements 

#1- if, elif, else syntax

#2 Comparison operators: ==, !=, >, <, >=, <=
#3  Logical operators:  and, or, not
#4  Nested if

#Example 1 — Even or Odd
"""
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

  

#ex- 3 - Grade Calculation 
marks=int(input("Enter your marks"))
if(marks>=90):
    print("A+ Grade")
elif(marks>=80):
    print("A grade")
elif(marks>=70):
    print("B Grade")
elif(marks>=60):
    print("c Grade")
elif(marks>=50):
    print("D grade")
else:
    print("Fail")
     
       

#ex -4 - Nested if :  ELigibility check

age=int(input("Enter you age"))
if(age>=18):
    has_id=input("Do you have Id card? (Yes / No)")
    if(has_id=="Yes"):
      print("Eligible to give vote")
    else:
      print("You Need Id card")
else:
    print("You are not Eligible to vote:yet")


    """

