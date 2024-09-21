from Expense import *
from ExpenseTracker import *

tracker = ExpenseTracker()

tracker.add_expense(Expense(100, "Food", "2024-09-19", "Lunch at cafe"))
tracker.add_expense(Expense(130, "Groceries", "2024-09-19", "Super market"))
tracker.add_expense(Expense(70, "Medicine", "2024-09-19", "Medicine for cold and fever"))
tracker.add_expense(Expense(100, "Transport", "2024-09-19", "Bus fare"))

print("All Expenses: ")
tracker.view_expenses

print("\nFiltered by category 'Food' :")
tracker.view_expenses(filter_by="Food")

print("\nTotal Spending on Food")
print(tracker.get_total_spending(filter_by="Food"))

print("\nExpense Report:")
report = tracker.generate_report()
for category, total in report.items():
    print(f"{category}: {total}")

tracker.delete_expense(1)

print("\nExpenses after deletion:")
tracker.view_expenses()