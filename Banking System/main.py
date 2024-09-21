from currentaccount import *
from savingsaccount import *
from BankAccount import *
from Bank import *

my_bank = Bank()

my_bank.create_account("Savings","Sourav", 5000)
my_bank.create_account("Current", "Singh", 2000)

account = my_bank.find_account(1)
if account:
    account.deposit(1000)
    account.check_balance()

savings_account = my_bank.find_account(1)
if isinstance(savings_account, SavingsAccount):
    savings_account.apply_interest()

current_Account = my_bank.find_account(2)
if isinstance(current_Account, CurrentAccount):
    current_Account.withdraw(2500)

my_bank.display_all_accounts()