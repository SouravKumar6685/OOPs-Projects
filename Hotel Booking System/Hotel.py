from Room import *
from Booking import *
from Customer import *

class Hotel:

    def __init__(self, name):
        self.hotel_name = name
        self.rooms = []
        self.bookings = []
    
    #add room
    def add_room(self, room):
        self.rooms.append(room)
    

    # Available rooms
    def get_available_rooms(self):
        return [room for room in self.rooms if room.is_available]
    

    #Make Booking
    def make_bookings(self, customer, room, check_in, check_out):

        if room.is_available:
            upgraded_room = self.check_for_room_upgrade(room)
            if upgraded_room:
                room = upgraded_room
                print(f"Room upgraded tp {room.room_type}")

            booking = Booking(customer,room, check_in, check_out)
            self.bookings.append(booking)
            room.mark_unavailable()


            booking.apply_discount()

            print(f"Booking confirmed for {customer.name} in room {room.room_number}")

        else:
            print("Room is not available")
    

    # Upgrade Room
    def check_for_room_upgrade(self, room):
        room_type_order = ["Single","Double","Suite"]
        current_type_index = room_type_order.index(room.room_type)

        for higher_type in room_type_order[current_type_index +1]:
            for available_room in self.get_available_rooms():
                if available_room.room_type == higher_type:
                    return available_room
        return None
    

    # Cancel Booking
    def cancel_booking(self, booking):
        booking.room.mark_available()
        self.bookings.remove(booking)
        print(f"Booking cancelled for {booking.customer.name}. Refund amount: Rs{booking.calculate_refund()}.")
