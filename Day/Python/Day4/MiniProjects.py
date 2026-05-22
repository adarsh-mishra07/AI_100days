"""
#Project -1 

num1=float(input("Enter the first nmbr"))
op=input("Enter the operator (+ , - , * , /)")
num2=float(input("Enter the second nmbr"))

if op=='+':
    print(num1+num2)
elif(op=='-'):
    print(num1-num2)
elif(op=='*'):
    print(num1*num2)
elif(op=='/'):
  if(num2!=0):
    print(num1/num2)
  else:
     print("Error : Division by Zero")
else:
    print("Invallid Operator!")

    """

#project 2  -  ATM

balance=5000
print("Welcome to ATM")
print("1.Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice=int(input("Enter you choice"))

if(choice==1):
    print("your balance is rs",balance)
elif choice==2:
    deposit=int(input("Enter amount to deposits:"))
    balance +=deposit
elif choice==3:
    withdraw=int(input("Enter amount withdraw"))
    if withdraw <=balance:
        balance-=withdraw
        print("Please collect your cash. Remaining",balance)
    else:
        print("Insufficient Balance !")
else:
    print("INvallid choice !")