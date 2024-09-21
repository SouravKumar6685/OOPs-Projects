import random

class PaymentGateway:

    def process_payment(Self, amount):
        print("Processing payment of Rs{amount}...")

        success = random.choice([True, False])
        if success:
            print("Payment succesful!\n")
            return True
        else:
            print("Payment failed. Please try again.\n")
            return False
    
