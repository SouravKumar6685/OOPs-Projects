from Expense import *

class ExpenseTracker:

    def __init__(self):
        self.expenses = []


    # Add expense    
    def add_expense(self, expense):
        self.expenses.append(expense)
    

    # Check expenses
    def view_expenses(self, filter_by=None):
        if filter_by:
            filtered_expenses = [expense for expense in self.expenses if expense.category == filter_by]
            for expense in filtered_expenses:
                print(expense)
        else:
            for expense in self.expenses:
                print(expense)
    
    # delete expense
    def delete_expense(self, index):
        if 0 <= index <= len(self.expenses):
            removed_expense = self.expenses.pop(index)
            print(f"Removed: {removed_expense}")
        else:
            print("Invalid index!")
    

    # total spending
    def get_total_spending(self, filter_by=None):
        if filter_by:
            return sum(expense.amount for expense in self.expenses if expense.category == filter_by)
        else:
            return sum(expense.amount for expense in self.expenses)
    
    # generate report
    def generate_report(self):
        report = {}
        for expense in self.expenses:
            if expense.category in report:
                report[expense.category] += expense.amount
            else:
                report[expense.category] = expense.amount
        return report

