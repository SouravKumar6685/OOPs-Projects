from BankAccount import *

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate = 0.03):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of Rs {interest} applied. New balance: Rs {self.balance}")
        