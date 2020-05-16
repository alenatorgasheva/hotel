class Room:
    """"""
    breakfast = 280.0
    half_board = 1000.0
    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def isfreeroom(self):
        pass

    def countprice(self):
        pass

    @staticmethod
    def max_price(room_prices):
        for i in range(len(room_prices)):
            for j in range(i, len(room_prices) - 1):
                if room_prices[j][0] < room_prices[j + 1][0]:
                    room_prices[j], room_prices[j + 1] = room_prices[j + 1], room_prices[j]
        return room_prices

    @staticmethod
    def min_capacity(lst_rooms):
        """lst_rooms - копия списка экземпляров класса рум
        ищем наименьшую вмещаемость из подходящих комнат (4 задача)"""
        rooms_capacity = []
        for room in lst_rooms:
            rooms_capacity.append([room.max_capacity, room])
        rooms_capacity.sort(key=lambda i: i[0])
        min_capacity = rooms_capacity[0][0]
        return min_capacity

    @staticmethod
    def lst_room_price(lst_rooms, min_capacity):
        room_price = []
        for room in lst_rooms:
            if room.max_capacity == min_capacity:
                room_price.append([room.price, room])
        return room_price
        # функция выполняет 4-ю задачу возвращает список (1)
        # [[цена комнаты, экземпляр класса комнат],[цена, экземпляр] и тд]