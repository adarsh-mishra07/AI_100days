name="Adarsh"
age=21
height=5.9
is_coder=True
print(f"My name is {name}, age:{age}, height:{height}, Coder: {is_coder}")

print(type(age))


# 1 -Write a program that takes your name and age as input and prints a sentence.
# 2- Make a calculator that adds, subtracts, multiplies, and divides two numbers.
# 3- Explore type() function for different variables.

#1st question 
name = (input("Enter the name"))
age= int(input("Enter the age"))
print(f"My name is {name} and age is {age}")

#2nd question - calculator 

num1=int(input("Enter the number 1"))
num2=int(input("Enter the number 2"))

add= num1+num2
print(f"Add={add}")

sub=num1-num2
print(f"Sum={sub}")

Mul=num1*num2
print("Mul:{Mul}")

if(num1>num2):
    div=num1/num2
    print(f"div={div}")
else:
     div=num2/num1
     print(f"div={div}")

#3rd question 
print(type(add))
print(type(name))
