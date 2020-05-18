# Case - study
# This program makes hotel room reservations.

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

from client import Client
from room import Room
import codecs
import copy


def main():
# 1
    list_of_rooms = []
    with codecs.open('fund.txt', 'r', encoding='utf-8') as file:
        for string in file.readlines():
            string = string.split()
            room = Room(string[0], string[1], string[2], string[3])
            list_of_rooms.append(room)  # Список экземпляров класса Room
# 2     ERROR
    list_of_clients = []
    with codecs.open('booking.txt', 'r', encoding='utf-8') as file:
        for string in file.readlines():
            string = string.split()

# в строке ниже TypeError
            client = Client(string[1], string[2], string[3], string[7], string[5], string[6])
            list_of_clients.append(client)  # Список экземпляров класса Client
            lst_rooms = copy.deepcopy(list_of_rooms)  # Здесь должна быть копия экземпляров

# 3
            for room in list_of_rooms:
                # Проверка дат
                if client.dates() & room.booked_date != 0:
                    lst_rooms.remove(room)
                    continue

                # Проверка мест
                if room.max_capacity < client.capacity:
                    lst_rooms.remove(room)
                    continue

                # Проверка цены
                if room.price > client.money:
                    lst_rooms.remove(room)
                    continue

    #    client = Client()
    min_capacity = Room.min_capacity(lst_rooms)
    rooms_w_price = Room.lst_room_price(lst_rooms, min_capacity)  # список (1)
    client.calc_new_price(rooms_w_price, min_capacity)
    # выбрали комнату
    chosen_room = Room.max_price(rooms_w_price)[0][1]
    price_chosen_room = Room.max_price(rooms_w_price)[0][0]


main()
