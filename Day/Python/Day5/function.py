#Defining & Calling Functions

def greet():
    print("Hello")


#Parameters & Return Values

def add(a,b):
    return a+b
result=add(10,5)
print("Sum =",result)

#defualt Arguments

def wel(name="Guest"):
    print(f"Welcome my {name}")
wel()
wel("Adarsh")

#keyboard Argument
def intro(name,age):
    print(f"My name is {name} and {age} years old.")
intro(age=21,name="Adarsh")

#variable length Argument (args* , **kwargs)
def total(*args):
    print(sum(args))
total(10,20,30)

#lambda (Anonymous) Function
square = lambda x: x**2
print(square(5))

#scope of variables (Local vs Global)
x=10
def change():
    x=5
    print("Inside:",x)
change()
print("Outside:",x)




