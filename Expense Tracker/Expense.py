class Expense:

    def __init__(self, amount, category, date, description=""):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
    
    # Details 
    def get_details(self):
        return{
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    def edit_expense(self, amount=None, category=None, date=None, description=None):
        if amount:
            self.amount = amount
        if category:
            self.category = category
        if date:
            self.date = date
        if description:
            self.description = description
        
    def __str__(self):
        return f"{self.date} | {self.category} : {self.amount} | {self.description}"
    