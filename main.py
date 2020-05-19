# Case - study
# This program makes hotel room reservations.

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (30%).

from client import Client
from room import Room
import codecs
import random

# Choosing the language
language = input('Choose your language:\n1. English\n2. Russian\n').lower()
while True:
    if language == 'english' or language == 'eng' or \
            language == 'e' or language == '1':
        import lc_eng as lc

        break
    elif language == 'russian' or language == 'rus' or \
            language == 'r' or language == '2':
        import lc_rus as lc

        break
    language = input('Please, choose language from proposed: ')


def end_of_day(day, list_of_rooms):
    """
    Printing day results.
    :param day: date
    :param list_of_rooms: list of rooms
    :return: None
    """
    today = set()
    today.add(day)
    room_types = {'одноместный': 0, 'двухместный': 0, 'полулюкс': 0, 'люкс': 0}
    types_of_busy_rooms = {'одноместный': 0, 'двухместный': 0, 'полулюкс': 0,
                           'люкс': 0}
    busy_rooms = 0
    free_rooms = 0
    for room in list_of_rooms:
        if not room.isfreeroom(today):
            busy_rooms += 1
            types_of_busy_rooms[room.type] += 1
            room_types[room.type] += 1
        else:
            free_rooms += 1
            room_types[room.type] += 1

    print('=' * 120)
    print(lc.TXT_END.format(day))
    print(lc.TXT_BUSY_ROOMS.format(busy_rooms))
    print(lc.TXT_FREE_ROOMS.format(free_rooms))
    print(lc.TXT_CATEGORIES)
    print(lc.TXT_TYPE_1.format(types_of_busy_rooms['одноместный'],
                               lc.TXT_FROM, room_types['одноместный']))
    print(lc.TXT_TYPE_2.format(types_of_busy_rooms['двухместный'],
                               lc.TXT_FROM, room_types['двухместный']))
    print(lc.TXT_TYPE_3.format(types_of_busy_rooms['полулюкс'],
                               lc.TXT_FROM, room_types['полулюкс']))
    print(lc.TXT_TYPE_4.format(types_of_busy_rooms['люкс'],
                               lc.TXT_FROM, room_types['люкс']))
    print(lc.TXT_OCCUPANCY.format(round(
        (busy_rooms / (busy_rooms + free_rooms)) * 100), 2))
    print(lc.TXT_INCOME_1.format(Room.income, lc.TXT_RBL))
    print(lc.TXT_INCOME_2.format(Room.lost_income, lc.TXT_RBL))


def booking_result(room, result, string, client, price_chosen_room):
    """
    Booking room.
    :param room: instance of class Room
    :param result: result of finding room and booking decision
    :param string: information about client from file
    :param client: instance of class Client
    :param price_chosen_room: price of chosen room
    :return: None
    """
    if price_chosen_room == room.price or room.price * 0.7:
        conditionals = 'без питания'
    elif price_chosen_room == room.price + 1000 or room.price * 0.7 + 1000:
        conditionals = 'полупансион'
    else:
        conditionals = 'завтрак'
    print('-' * 120)
    print(lc.TXT_REQUEST)
    print(' '.join(string))
    if result == 0:
        print(lc.TXT_NO_OFFERS)
        return
    print(lc.TXT_FOUND.format(room, room.max_capacity, client.capacity,
                              conditionals, price_chosen_room))
    if result:
        print(lc.TXT_AGREE)
    else:
        print(lc.TXT_DECLINE)


def main():
    # Reading information about rooms.
    list_of_rooms = []
    today = ''
    with codecs.open('fund.txt', 'r', encoding='utf-8') as file:
        for string in file.readlines():
            string = string.split()
            room = Room(string[0], string[1], string[2], string[3])
            list_of_rooms.append(room)

    # Booking process.
    list_of_clients = []
    with codecs.open('booking.txt', 'r', encoding='utf-8') as file:
        for string in file.readlines():
            # Reading information about client.
            string = string.split()
            client = Client(string[1], string[2], string[3], string[4], string[7], string[5], string[6])
            list_of_clients.append(client)
            lst_rooms = []

            # Finding correct rooms.
            for room in list_of_rooms:
                # Checking free dates.
                if room.isfreeroom(client.dates()):
                    # Checking available capacity.
                    if room.max_capacity >= client.capacity:
                        # Checking available price.
                        if room.price <= client.money:
                            lst_rooms.append(room)

            if len(lst_rooms) != 0:
                # Finding the most expensive room from list of available rooms.
                min_capacity = Room.min_capacity(lst_rooms)
                rooms_w_price = Room.lst_room_price(lst_rooms, min_capacity)
                client.calc_new_price(rooms_w_price, min_capacity)
                chosen_room = Room.max_price(rooms_w_price)[0][1]
                price_chosen_room = Room.max_price(rooms_w_price)[0][0]
                income = float(price_chosen_room * client.capacity * client.count_days)

                # Getting and printing result of booking process.
                if lst_rooms:
                    if random.random() > 0.25:
                        # Booking process succeed.
                        room.booked_date.update(room.booked_date, client.dates())
                        Room.income += income
                        chosen_room.booked_date.update(chosen_room.booked_date, client.dates())
                        result = True

                    else:
                        # Client canceled offer.
                        Room.lost_income += income
                        result = False
            else:
                # No available rooms.
                Room.lost_income += client.money * client.count_days
                result = 0
            booking_result(chosen_room, result, string, client, price_chosen_room)

            # Printing day results.
            if today:
                if today != string[0]:
                    end_of_day(today, list_of_rooms)
                    today = string[0]
                    Room.lost_income = 0
                    Room.income = 0
            else:
                today = string[0]
        end_of_day(today, list_of_rooms)


main()
