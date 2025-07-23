import random
from abc import ABC, abstractmethod

# Abstract class with encapsulation
class BankAccount(ABC):
    def __init__(self, owner, bank_name):
        self.owner = owner
        self.bank_name = bank_name
        self.__balance = 0
        self.account_number = random.randint(100000, 999999)
        print(f"\n🏦 Welcome to {self.bank_name}, {self.owner}!")
        print(f"✅ Your new account number is: {self.account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"💰 {amount} deposited. New balance: {self.__balance}")
        else:
            print("❌ Invalid deposit amount.")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):  # protected
        self.__balance += amount

# Simple Savings Account with overridden withdraw
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._update_balance(-amount)
            print(f"💸 {amount} withdrawn. Remaining balance: {self.get_balance()}")
        else:
            print("❌ Insufficient funds.")

# Store accounts in a dictionary
accounts = {}

# Main simple menu
def main():
    print("====== Simple Bank System ======")
    bank_name = input("Name your bank: ")
    name = input("Enter your name: ")

    # Create account
    account = SavingsAccount(name, bank_name)
    accounts[account.account_number] = account

    while True:
        print("\n📋 Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '4':
            print("👋 Thank you for banking with us!")
            break

        try:
            acc_num = int(input("Enter your account number: "))
            if acc_num not in accounts:
                print("❌ Account not found.")
                continue

            user_acc = accounts[acc_num]

            if choice == '1':
                amt = float(input("Enter amount to deposit: "))
                user_acc.deposit(amt)

            elif choice == '2':
                amt = float(input("Enter amount to withdraw: "))
                user_acc.withdraw(amt)

            elif choice == '3':
                print(f"💼 Account Balance: {user_acc.get_balance()}")

            else:
                print("❌ Invalid choice.")

        except ValueError:
            print("❌ Please enter valid numbers only.")

# Run the app
main()
