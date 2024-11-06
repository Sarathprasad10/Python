#Create a simple banking application by using inheritance.

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and within the available balance.")

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and within the available balance and overdraft limit.")

def main():
    accounts = {}

    while True:
        print("\nMenu:")
        print("1. Create Savings Account")
        print("2. Create Checking Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Add Interest to Savings Account")
        print("7. Display Account Details")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            acc_balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate (e.g., 0.01 for 1%): "))
            accounts[acc_num] = SavingsAccount(acc_num, acc_holder, acc_balance, interest_rate)
            print("Savings account created successfully.")

        elif choice == "2":
            acc_num = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            acc_balance = float(input("Enter initial balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            accounts[acc_num] = CheckingAccount(acc_num, acc_holder, acc_balance, overdraft_limit)
            print("Checking account created successfully.")

        elif choice == "3":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[acc_num].deposit(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[acc_num].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "5":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                balance = accounts[acc_num].get_balance()
                print(f"Account balance: ${balance:.2f}")
            else:
                print("Account not found.")

        elif choice == "6":
            acc_num = input("Enter account number: ")
            if acc_num in accounts and isinstance(accounts[acc_num], SavingsAccount):
                accounts[acc_num].add_interest()
            else:
                print("Savings account not found.")

        elif choice == "7":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                accounts[acc_num].display()
            else:
                print("Account not found.")

        elif choice == "8":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
