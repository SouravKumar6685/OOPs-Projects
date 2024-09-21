

class Order:
    order_id_counter = 1

    def __init__(self, customer, items):
        self.order_id = order_id_counter
        Order.order_id_counter +=1
        self.customer = customer
        self.items = items
        self.status = "Processing"
        self.status_updates = [("Processing", "Order is being processed.")]

    # Display order
    def display_order(self):
        print(f"Order Id: {self.order_id}, Status: {self.status}")
        print("Items:")
        for item, qty in self.items:
            print("f{item.name} - Quantity: {qty}")
        print("\n")
    
    # Track Order
    def track_order(self):
        print(f"Tracking Order ID: {self.order_id}")
        for status, message in self.status_updates:
            print(f"Status: {status}, Message: {message}")
        print("\n")
    
    # Add Status
    def add_Status_update(self, new_Status, message):
        self.status_updates.append((new_Status, message))
        self.status = new_Status
