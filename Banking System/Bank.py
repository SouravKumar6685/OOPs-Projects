from currentaccount import *
from savingsaccount import *
from BankAccount import *


class Bank:

    def __init__(self):
        self.account_list = []
    
    def create_account(self, account_type, account_holder, initial_deposit = 0):
        account_number = len(self.account_list) + 1
        if account_type == "Savings":
            account = SavingsAccount(account_number, account_holder, initial_deposit)
        elif account_type == "Current":
            account = CurrentAccount(account_number, account_holder, initial_deposit)
        else:
            print("Invalid account type!")
            return

        self.account_list.append(account)
        print(f"{account_type} Account created {account_holder} with Account Number {account_number}")

    def find_account(self, account_number):
        for account in self.account_list:
            if account.account_number == account_number:
                return account
        
        print("Account not found!")
        return None
 
    def display_all_accounts(self):
        if not self.account_list:
            print("No accounts found!")
        for account in self.account_list:
            account.display_account_details()
            print("-"*20)