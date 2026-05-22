#Assign 14

#1

"""
nmbr=int(input("Enter the nmbr"))
if nmbr>99 and nmbr<1000:
    print("Number is three digit: ",nmbr)

"""

#3

"""
print("1. Odd-even")
print("2. Positive ,negative and zero")
print("3.Simple intrest")
print("4.Qudratic Equation",)
print("\n")
choice=int(input("Enter the choice : "))

match choice:
    case 1:
        numbr=int(input("Enter the numbr"))
        if numbr%2==0:
            print("Ever nmbr")
        else:
            print("Odd")
    case 2:
        numbr=int(input("Enter the numbr"))
        if numbr>0:
            print("Positive nmbr")
        elif numbr==0:
            print("It is 0")
        else:
            print("numbr is negative")
    case 3:
        principle=int(input("Enter the principle"))
        rate=int(input("Enter the rate"))
        time=int(input("Enter the time"))
        Si=(principle*rate*time)/100
        print("SI is :",Si)
    
    case 4:
        b=int(input("Enter the b"))
        a=int(input("Enter the a"))
        c=int(input("Enter the c"))
        D = b*b - 4*a*c
        print("D is :",D)
    
    case _:
        print("Invalid input")
            
"""


#4 evaluate the data type
"""
input=eval(input("Enter the value:"))

match input:
    case bool():
        print("Thursday")
    case int():
        print("Monday")
    case float():
        print("Wednesday")
    case complex():
        print("Tuesday")
    case _:
        print("Invalid input")

        """

#5 string  take from user

str=input("Enter the string:")
match str:
    case str if str in "Mysirg":
          print("One")
    case str if str in "Education":
          print("Two")
    case str if str in "Services":
          print("Three")
    case _:
        print("Invalid input")
       