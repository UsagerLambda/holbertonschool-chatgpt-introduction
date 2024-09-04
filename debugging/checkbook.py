#!/usr/bin/env python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("\033[92mCurrent Balance: ${:.2f}\033[0m".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("\033[93mInsufficient funds to complete the withdrawal.\033[0m")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("\033[92mCurrent Balance: ${:.2f}\033[0m".format(self.balance))

    def get_balance(self):
        print("\033[92mCurrent Balance: ${:.2f}\033[0m".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("\033[93mPlease enter a positive amount.\033[0m")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("\033[93mInvalid input. Please enter a numeric value.\033[0m")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("\033[93mPlease enter a positive amount.\033[0m")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("\033[93mInvalid input. Please enter a numeric value.\033[0m")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("\033[93mInvalid command. Please try again.\033[0m")

if __name__ == "__main__":
    main()
