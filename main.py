from datetime import date
from manage import find_available_room_for_customer, generate_rooms, book_room_for_customer, checkout_guest
from guest import Guest

if __name__ == "__main__":
    # Hotel structure
    # First three values are number of rooms with 1, 2, 3 beds respectively in level 1
    # Second three values are number of rooms with 1, 2, 3 beds respectively in level 2
    count_of_rooms_by_type = [2, 3, 4, 3, 4, 5]

    rooms = generate_rooms(count_of_rooms_by_type)
    
    # New guests
    new_guest = Guest('A', False, 3, 2, 1000, date(2020, 9, 27), date(2020, 9, 28))
    new_guest1 = Guest('B', True, 1, 2, 500, date(2020, 9, 27), date(2020, 9, 29))

    # Find available rooms
    find_available_room_for_customer(rooms, new_guest)
    find_available_room_for_customer(rooms, new_guest1)

