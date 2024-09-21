# Cart Class
class Cart:
    def __init__(self):
        self.items = []  # Initialize items as an empty list
        self.total_price = 0.0  # Initialize total price as 0.0
    
    def add_to_cart(self, product, quantity):
        if product.stock_quantity >= quantity:
            self.items.append((product, quantity))  # Add (product, quantity) tuple to items
            self.total_price += product.price * quantity
            product.update_stock(-quantity)
            print(f"Added {quantity} of {product.name} to cart.\n")
        else:
            print(f"Insufficient stock for {product.name}.\n")
    
    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.total_price -= item[0].price * item[1]
                self.items.remove(item)
                product.update_stock(item[1])
                print(f"Removed {product.name} from cart.\n")
                break
    
    def calculate_total(self):
        print(f"Total price: ${self.total_price}\n")
    
    def checkout(self):
        if not self.items:
            print("Your cart is empty.\n")
        else:
            print(f"Checking out with total price: ${self.total_price}")
            self.items.clear()
            self.total_price = 0.0
