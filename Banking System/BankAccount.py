class BankAccount:
    # Constructor
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs {amount} deposited. New balance: Rs {self.balance}")
        else:
            print("Deposit amount must be positive!")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Rs {amount} withdrawn. New balance: Rs {self.balance}")
        
        else:
            print("Insufficient balance, please check amount once!")
        

    # Check balance
    def check_balance(self):
        print(f"Amount Balance: Rs {self.balance}")
        return self.balance

    # Display account display
    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: {self.balance}")