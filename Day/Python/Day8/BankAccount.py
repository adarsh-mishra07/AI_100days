class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} ₹ deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} ₹ withdrawn successfully.")
        else:
            print("❌ Insufficient Balance!")

    def showBal(self):
        print(f"💰 Current Balance: {self.balance} ₹")

# Menu-driven interface
def main():
    acc = BankAccount()
    while True:
        print("\n===== Bank Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amt = int(input("Enter amount to deposit: "))
            acc.deposit(amt)
        elif choice == '2':
            amt = int(input("Enter amount to withdraw: "))
            acc.withdraw(amt)
        elif choice == '3':
            acc.showBal()
        elif choice == '4':
            print("👋 Thank you for using our service!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the program
main()