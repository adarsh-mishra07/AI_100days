"""
Playing with Variables

Q1

Write a python script containing a variable with some integer value, print value of this variable.

Q2

Write a python script to print the value of a variable. Variable contains your name as data.

Q3

Write a python script to print values of three variables, each in a new line. All three variables are filled with some integer values.

Q4

Create 5 variables each of them containing different types of data (like 35, True, "MySirG", 5.46, 3+4j, etc). Write a python script to print values of all the variables along with their data types.

Q5

Create three variables and assign current date to them, first variable contains day number, second variable contains month number and third variable contains year number. Write a python script to display date in standard way (e.g. 29/11/2022).

"""
#Q1
a=10
print(a)

#Q2
name="Adarsh Mishra"
print("My name:",name,"\n")
#Q3
b=3
c=2
d=5
print(b)
print(c)
print(d)


#Q4
inte=35
boo=True
Teacher="MySirG"
dasamlav=5.46
com=3+4j

print("Integer value:",inte,type(inte),"\n")
print("Boolean Value:",boo,type(boo),"\n")
print("String Value:",Teacher,type(Teacher),"\n")
print("dasamlav:",dasamlav,type(dasamlav),"\n")
print("Real and Imajinary value:",com,"+j",type(com),"\n")

#Q5
day=12
month=3
year=2026
print(f"{day}/{month}/{year}")