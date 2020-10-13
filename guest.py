class Guest:
    def __init__(self, name, is_disabled, bed_count, pets_count, balance, checkin_date, checkout_date):
        self.name = name
        self.is_disabled = is_disabled
        self.bed_count = bed_count
        self.pets_count = pets_count
        self.balance = balance
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.room_number = -1

    def set_room_number(self, room_number):
        self.room_number = room_number