from datetime import date
from guest import Guest
from room import Room 
import error
        
def find_available_room_for_customer(rooms, new_guest):
    book_succeed = False
    
    for room_number, room in enumerate(rooms):
        check_result = room.is_available_for_customer(new_guest)

        if check_result == True:
            book_room_for_customer(rooms, room_number, new_guest)
            new_guest.room_number = room_number
            book_succeed = True
            break

    if book_succeed == False:
        print(new_guest.name + ": Booking failed. " + check_result)
        return check_result

    return True

def book_room_for_customer(rooms, room_number, guest):
    rooms[room_number].checkin_date = guest.checkin_date
    rooms[room_number].checkout_date = guest.checkout_date
    print(guest.name + ": Booking succeed")
    
    return "Booking success"

def checkout_guest(rooms, guest):
    rooms[guest.room_number].checkin_date = None
    rooms[guest.room_number].checkout_date = None
    print(guest.name + ": checked out")

    return "Checked out"

def generate_rooms(count_of_rooms_by_type):
    rooms = [None] * sum(count_of_rooms_by_type)
    room_number = 0

    for i, room_count in enumerate(count_of_rooms_by_type):
        for j in range(room_count):
            if i % 3 == 0:
                price = 50
            elif i % 3 == 1:
                price = 75
            else:
                price = 90

            j = j
            rooms[room_number] = Room(int(i / 3) + 1, price, i % 3 + 1, None, None)
            room_number += 1

    return rooms
