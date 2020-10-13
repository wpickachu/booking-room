from datetime import date
from manage import find_available_room_for_customer, generate_rooms, checkout_guest
from guest import Guest
from room import Room
import error
import pytest

@pytest.mark.skip
def test_room_generation():
    rooms = generate_rooms([2, 3, 4, 3, 4, 5])
    assert len(rooms) == 21

def test_pay_checker():
    # PET_CHECK : If the number of pets is more than 2
    room = Room(1, 50, 1, None, None)
    new_guest = Guest('A', False, 1, 5, 60, date(2020, 9, 27), date(2020, 9, 28))
    assert Room.is_available_for_customer(room, new_guest) == error.PET_CHECK_ERROR

def test_handicap_checker():
    # HANDICAP_ERROR : If level is 2 and guest is disabled
    room = Room(2, 50, 1, None, None)
    new_guest = Guest('B', True, 1, 2, 60, date(2020, 9, 27), date(2020, 9, 28))
    assert Room.is_available_for_customer(room, new_guest) == error.HANDICAP_ERROR

def test_balance_checker():
    # BALANCE_ERROR : If user's balance is insufficient for room cost
    room = Room(1, 50, 1, None, None)
    new_guest = Guest('C', False, 1, 0, 10, date(2020, 9, 27), date(2020, 9, 28))
    assert Room.is_available_for_customer(room, new_guest) == error.BALANCE_ERROR

    room = Room(1, 50, 1, None, None)
    new_guest = Guest('C', False, 1, 2, 70, date(2020, 9, 27), date(2020, 9, 28))
    assert Room.is_available_for_customer(room, new_guest) == error.BALANCE_ERROR

def test_occupation_checker():
    # OCCUPATION_ERROR : If the room is already booked
    room = Room(1, 50, 1, date(2020, 9, 27), date(2020, 9, 28))
    new_guest = Guest('D', False, 1, 2, 90, date(2020, 9, 28), date(2020, 9, 30))
    assert Room.is_available_for_customer(room, new_guest) == error.OCCUPATION_ERROR

def test_bed_checker():
    # BED_ERROR : If the room doesn't have proper number of beds
    room = Room(1, 50, 1, date(2020, 9, 27), date(2020, 9, 28))
    new_guest = Guest('E', False, 2, 2, 90, date(2020, 9, 29), date(2020, 9, 30))
    assert Room.is_available_for_customer(room, new_guest) == error.BED_COUNT_ERROR

def test_find_available_room_for_customer_func():
    rooms = generate_rooms([1, 1, 1, 1, 1, 1])

    new_guest = Guest('F', True, 3, 2, 1000, date(2020, 9, 27), date(2020, 9, 28))  
    assert find_available_room_for_customer(rooms, new_guest) == True
    assert new_guest.room_number == 2

    new_guest1 = Guest('G', True, 3, 2, 1000, date(2020, 9, 27), date(2020, 9, 28))
    assert find_available_room_for_customer(rooms, new_guest1) == error.HANDICAP_ERROR

    # After checkout, the third room should be empty
    checkout_guest(rooms, new_guest)
    assert rooms[2].checkin_date == None 


