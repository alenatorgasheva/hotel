# Case - study
# This program

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

from client import Client
from room import Room


def main():
    client = Client()
    lst_rooms = []  # Здесь должна быть копия экземпляров
    min_capacity = Room.min_capacity(lst_rooms)
    rooms_w_price = Room.lst_room_price(lst_rooms, min_capacity)  # список (1)
    client.calc_new_price(rooms_w_price, min_capacity)
    # выбрали комнату
    chosen_room = Room.max_price(rooms_w_price)[1]
    price_chosen_room = Room.max_price(rooms_w_price)[0]


main()
