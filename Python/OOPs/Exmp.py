# Bank Management System using OOP in Python

class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. Current balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print(f"Account No: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}")


# Inheritance Example
class SavingsAccount(Account):
    def __init__(self, acc_no, name, balance=0, interest_rate=5):
        super().__init__(acc_no, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest of ₹{interest} added. New balance: ₹{self.balance}")


# Bank class manages all accounts
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self, acc_no, name, acc_type="savings"):
        if acc_no in self.accounts:
            print("Account already exists!")
            return
        if acc_type == "savings":
            self.accounts[acc_no] = SavingsAccount(acc_no, name)
        else:
            self.accounts[acc_no] = Account(acc_no, name)
        print(f"Account created successfully for {name}.")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)

    def display_all_accounts(self):
        print(f"\nAll Accounts in {self.bank_name}:")
        for acc in self.accounts.values():
            acc.display()
            print("-" * 30)


# -------- Main Program --------
def main():
    bank = Bank("State Bank of Python")

    while True:
        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Details")
        print("5. Display All Accounts")
        print("6. Add Interest (Savings Only)")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            acc_no = input("Enter account number: ")
            name = input("Enter account holder name: ")
            acc_type = input("Enter account type (savings/current): ").lower()
            bank.create_account(acc_no, name, acc_type)

        elif choice == '2':
            acc_no = input("Enter account number: ")
            acc = bank.get_account(acc_no)
            if acc:
                amt = float(input("Enter amount to deposit: "))
                acc.deposit(amt)
            else:
                print("Account not found!")

        elif choice == '3':
            acc_no = input("Enter account number: ")
            acc = bank.get_account(acc_no)
            if acc:
                amt = float(input("Enter amount to withdraw: "))
                acc.withdraw(amt)
            else:
                print("Account not found!")

        elif choice == '4':
            acc_no = input("Enter account number: ")
            acc = bank.get_account(acc_no)
            if acc:
                acc.display()
            else:
                print("Account not found!")

        elif choice == '5':
            bank.display_all_accounts()

        elif choice == '6':
            acc_no = input("Enter account number: ")
            acc = bank.get_account(acc_no)
            if isinstance(acc, SavingsAccount):
                acc.add_interest()
            else:
                print("Interest applicable only for savings accounts!")

        elif choice == '7':
            print("Thank you for using our Bank Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
