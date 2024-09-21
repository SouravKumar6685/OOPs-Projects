


class Customer:

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.booking_history = []

    def make_payment(self, amount):
        print(f"Processing payment of Rs{amount} for {self.name}")
