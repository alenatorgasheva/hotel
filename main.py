# Case - study
# This program

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

from client import Client
from room import Room
import codecs
import copy

def main():
    list_of_rooms = []
    with codecs.open('fund.txt', 'r', encoding='utf-8') as file:
        for string in file.readlines():
            string = string.split()
            room = Room(string[0], string[1], string[2], string[3])
            list_of_rooms.append(room) # Список экземпляров класса Room

    list_of_clients = []
    with codecs.open('booking.txt', 'r', encoding='utf-8') as file:
        for string in file.readlines():
            string = string.split()
            client = Client(string[1], string[2], string[3], string[7], string[5], string[6])
            list_of_clients.append(client) # Список экземпляров класса Client

#    client = Client()
    lst_rooms = copy.deepcopy(list_of_rooms)  # Здесь должна быть копия экземпляров
    min_capacity = Room.min_capacity(lst_rooms)
    rooms_w_price = Room.lst_room_price(lst_rooms, min_capacity)  # список (1)
    client.calc_new_price(rooms_w_price, min_capacity)
    # выбрали комнату
    chosen_room = Room.max_price(rooms_w_price)[0][1]
    price_chosen_room = Room.max_price(rooms_w_price)[0][0]


main()
