import error

class Room:
    def __init__(self, level, price, bed_count, checkin_date, checkout_date):
        self.level = level
        self.price = price
        self.bed_count = bed_count
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
    
    def is_available_for_customer(self, guest):
        # Pet check
        if guest.pets_count > 2:
            return error.PET_CHECK_ERROR

        # Handicap check
        if self.level == 2 and guest.is_disabled == True:
            return error.HANDICAP_ERROR

        # Balance check
        if self.price > guest.balance or guest.pets_count <= 2 and self.price + 20 * guest.pets_count > guest.balance: 
            return error.BALANCE_ERROR

        if self.bed_count != guest.bed_count:
            return error.BED_COUNT_ERROR
                    
        if self.bed_count == guest.bed_count and self.checkin_date != None and self.checkout_date != None:
            latest_start = max(self.checkin_date, guest.checkin_date)
            earlist_end = min(self.checkout_date, guest.checkout_date)
            delta = (earlist_end - latest_start).days + 1

            if delta > 0:
                return error.OCCUPATION_ERROR

        return True