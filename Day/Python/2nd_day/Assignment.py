class Assign:
 #Write a program to check whether a number is positive, negative or zero
 def checkPosNeg(self):
  num=int(input("Enter the nmbr"))
  if(num>0):print("Positive Number")
  if(num==0):
   print("Zero")
  else:
   print("Negative Number")

#Write a program to check if a year is leap year

 def checkLeap(self):
  year=int(input("Enter the year"))
  if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("Leap Year")
  else:
    print("Not Leap Year")

#Create a password strength checker (if len < 6 → weak, else → strong)
 def passChecker(self):
  password = input("Enter the Password: ")
  if len(password) < 6:
    print("Weak Password")
  else:
    print("Strong Password")

A1=Assign()
A1.checkPosNeg()
 
 

  
    

 