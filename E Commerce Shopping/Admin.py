from User import *

class Admin(User):

    def __init__(self, username, email, password, address):
        super().__init__(username, email, password, address)
    

    def add_product(self, product_list, product):
        product_list.append(product)
        print(f"Product {product.name} added to store.\n")
    
    # remove product
    def remove_product(Self, product_list, product_name):
        for product in product_list:
            if product.name == product_name:
                product_list.remove(product)
                print(f"Product {product_name} removed from store.\n")
                break
    

    # Update product
    def update_product(self, product, name=None , price=None, stock=None, description=None):
        if name:
            product.name = name
        if price:
            product.price = price
        if stock: 
            product.stock = stock
        if description:
            product.description = description
        print(f"Product {product.name} updated.\n")

    # update order status
    def update_order_Status(self, order, new_Status):
        order.status = new_Status
        print(f"Order ID {order.order_id} status updated to {new_Status}. \n")
    
