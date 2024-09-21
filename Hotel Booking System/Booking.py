from Room import *
from datetime import *
from Customer import *



class Booking(room):

    def __init__(self, customer, room, check_in, check_out):
        self.customer = customer
        self.room= room
        self.check_in_date = check_in
        self.check_out_date = check_out
        self.services = []
        self.total_price = self.calculate_total_price()
        self.discount_applied = False

    # Calculate toal price
    def calculate_total_price(self):
        days = (self.check_out_date - self.check_in_date).days
        return days*self.room.price_per_night
    
    # Apply Discount
    def apply_discount(self):
        days = (self.check_out_date - self.check_in_date).days
        if days > 7:
            self.total_price *= 0.9
            self.discount_applied = True
            print("10% discoount applied for long stay.")


    # Add serives
    def add_services(self, service):
        self.services.append(service)
        self.total_price += service.price
        print(f"Service {service.name} added. New total price: Rs{self.total_price}")

    
    # Calculate refund
    def calculate_refund(self):
        days_before_checkin = (self.check_in_date - date.today()).days
        if days_before_checkin >= 3:
            return self.total_price
        else:
            return self.total_price*0.5
        
    # Confirm Booking
    def confirm_booking(self):

        self.customer.booking_history.append(self)
        print(f"Booking confirmend for {self.customer.name} in room {self.room.room_number}")
    