


class room:

    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

    def mark_available(self):
        self.is_available = True
    
    def mark_unavailable(self):
        self.is_available = False