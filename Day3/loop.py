# 1️⃣ Sum of N Natural Numbers



sum=0
for i in range(1,11):
   sum=sum+i
print(sum)
#-----------------------------------------------------------------
# 2️⃣ Multiplication Table Generator

num=int(input("Enter the number for table"))
for i in range(1,11):
   print(f"{num}*{i}={num*i}")
   
#-----------------------------------------------------------


#3️⃣ Factorial Calculator

fact=1
num=int(input("Enter the number for factorial"))
for i in range(1,num+1):
    fact=fact*i
print(f"factorial of {num}  is {fact}")

#------------------------------------------------------------


#4 While Loop Practice
#Creating number guessing and countdown programs that show the power of conditions and loops together.
#while loop
# 4 While Loop Practice - Number Guessing Game

target = int(input("Enter your Target: ")) # You can set any target number
guess = int(input("Enter your guess: "))

while True:
    if guess < 0:
        print("Enter a positive number!")
    elif guess == target:
        print("🎉 Finally got it!")
        break
    else:
        print("Wrong guess! Try again.")
    
    guess = int(input("Enter your guess again: "))

#-------------------------------------------------------------------------

#5 - Pattern Printing Programs

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)
