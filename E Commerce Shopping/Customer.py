from User import *
from Cart import *
from PaymentGateway import *
from Order import *


class Customer(User):

    def __init__(self, username, email, password, address):
        super().__init__(username, email, password, address)
        self.cart = Cart()
        self.order_history = []
        self.payment_gateway = PaymentGateway()

    # Place order

    def place_order(self):

        if self.cart.items:
            if self.payment_gateway.process_payment(self.cart.total_price):
                order = order(self, self.cart.items)
                self.order_history.append(order)
                print("Order placed successfully!\n")
                self.cart.checkout()
            else:
                print("Order not placed due to payment failure.\n")
        else:
            print("Your cart is empty, cannot place an order.\n")

    def view_order_history(self):
        if self.order_history:
            for order in self.order_history:
                order.display_order()
        else:
            print("No order history.\n")


