
"""class bank:
    def __init__(self,balance):
        self.balance=balance
        print("Bank account created with balance:",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited:",amount)
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("Amount withdrawn:",amount)
        else:
            print("Insufficient balance")
        
B1=bank(1000)
B1.deposit(500)
print(B1.balance)
B1.withdraw(1700)
print

"""

#user defined exception class with the help of raise keyword
"""
class bank:
    def __init__(self,balance):  #it made init because it is constructor and it will be called when we create object of class
        self.balance=balance
        print("Bank account created with balance:",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited:",amount)
    def show_balance(self):
        print("Current balance:",self.balance)
    def withdraw(self,amount):
        if self.balance<amount:
            raise Exception("Insufficient balance")
        self.balance-=amount
        print("Amount withdrawn:",amount)
        
B1=bank(1000)
B1.deposit(500)
print(B1.balance)
B1.withdraw(1700)


"""


#custom exception class with the help of raise keyword

class AccountTransactionError(Exception):
    def __init__(self,msg="Transaction error"):   #it made init because it is constructor and it will be called when we create object of class
        self.msg=msg
    def __str__(self):  #it made str because it will return string when we print the object of class
        return self.msg
        
class bank:
    def __init__(self,balance):  #it made init because it is constructor and it will be called when we create object of class
        self.balance=balance
        print("Bank account created with balance:",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited:",amount)
    def show_balance(self):
        print("Current balance:",self.balance)
    def withdraw(self,amount):
        if self.balance<amount:
            raise AccountTransactionError("Insufficient balance")
        self.balance-=amount
        print("Amount withdrawn:",amount)

try:
 B1=bank(1000)
 B1.deposit(500)
 print(B1.balance)
 B1.withdraw(1700)
except AccountTransactionError as e:
    print(e)
print("Transaction completed")



