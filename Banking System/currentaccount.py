from BankAccount import *

class CurrentAccount(BankAccount):
    
    def __init__(self, account_number, account_holder, balance = 0, overdraft_limit = 10000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Rs {amount} withdrawn. New balance: Rs {self.balance}")
        else:
            print("Withdrawn exceeds overdraft limit!")