from Room import *
from Customer import *
from Booking import *
from Hotel import *
from datetime import *

class Service:

    def __init__(self, name, price):
        self.name = name
        self.price = price



hotel = Hotel("Falaknama")
room1 = room(101, "Single", 3000)
room2 = room(102, "Double", 4500)
room3 = room(103, "Suite", 9000)

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

customer = Customer("Sourav","7671036655")
check_in = date(2024, 9, 19)
check_out = date(2024, 9, 25)

hotel.make_bookings(customer, room1, check_in, check_out)

booking = hotel.bookings[0]
room_Service = Service("Room Services", 500)
laundary = Service("Laundary", 300)
booking.add_services(room_Service)
booking.add_services(laundary)

