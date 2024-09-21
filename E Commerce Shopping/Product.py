

class Product:

    def __init__(self, name, price, category, stock_quantity, description):
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity
        self.description = description

    # Quantity updation
    def update_stock(self, quantity):
        self.stock_quantity += quantity
    
    # discount
    def apply_discount(self, percentage):
        self.price -= self.price * (percentage/100)
    

    #  Display details
    def display_details(self):
        print(f"Product: {self.name} , price : Rs{self.price}, Stock: {self.stock_quantity}, Category: {self.category}")
        print(f"\nDescription: {self.description}\n")
