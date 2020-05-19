# Case - study
# This program makes hotel room reservations.

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

from client import Client
from room import Room
import codecs
import copy
import random


def main():
    # 1
    list_of_rooms = []
    with codecs.open('fund.txt', 'r', encoding='utf-8') as file:
        for string in file.readlines():
            string = string.split()
            room = Room(string[0], string[1], string[2], string[3])
            list_of_rooms.append(room)  # Список экземпляров класса Room
    # 2
    list_of_clients = []
    with codecs.open('booking.txt', 'r', encoding='utf-8') as file:
        for string in file.readlines():
            string = string.split()

            client = Client(string[1], string[2], string[3], string[4], string[7], string[5], string[6])
            list_of_clients.append(client)  # Список экземпляров класса Client
            lst_rooms = copy.deepcopy(list_of_rooms)

            # 3
            for room in list_of_rooms:
                # Проверка дат
                if room.isfreeroom(client.dates()):
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
            min_capacity = Room.min_capacity(lst_rooms)
            rooms_w_price = Room.lst_room_price(lst_rooms, min_capacity)  # список (1)
            client.calc_new_price(rooms_w_price, min_capacity)
            # выбрали комнату
        # 7
            if len(lst_rooms) != 0:
                chosen_room = Room.max_price(rooms_w_price)[0][1]
                price_chosen_room = Room.max_price(rooms_w_price)[0][0]
                income = float(price_chosen_room * client.capacity * client.count_days)
                for _ in lst_rooms:
                    if random.random > 0.25:
                        # Клиент согласен
                        room.booked_date.add(client.dates())
                        Room.income += income
                        # здесь мы должны добавлять дни
                        chosen_room.booked_date.update(chosen_room.booked_date, client.dates())

                    else:
                        # Клиент сам отказался
                        Room.lost_income += income
            else:
                # Отказ, тк предложений нет
                Room.lost_income += client.money * client.count_days
        # а где вывод типа принята заявка и тд ???????????????
        # 8
            if today:
                if today != string[0]:
                    Room.end_of_day(today,list_of_rooms)
                    today = string[0]
                    Room.lost_income = 0
                    Room.income = 0
            else:
                today = string[0]


main()
