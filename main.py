# Case - study
# This program

# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

import client
import room


def max_price(room_prices):
    for i in range(len(room_prices)):
        for j in range(i, len(room_prices) - 1):
            if room_prices[j][0] < room_prices[j + 1][0]:
                room_prices[j], room_prices[j + 1] = room_prices[j + 1], room_prices[j]
    return room_prices


def main():
    pass


main()
