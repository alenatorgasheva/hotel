import client

class Room:
    """ Класс номеров отеля """
    breakfast = 280.0
    half_board = 1000.0

    type_of_room = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    comfort_degree = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}

    def __init__(self, number, type, max_capacity, comfort):
        """Метод инициализации"""
        self.number = number
        self.type = type
        self.max_capacity = max_capacity
        self.comfort = comfort
        self.booked_date = set()
        self.price = Room.type_of_room[self.type] * Room.comfort_degree[self.comfort]

    def needed_dates(self, ):
        """Метод определения свободна ли комната"""
        if client.dates() & self.booked_date == 0:
            return True
        else:
            return False

    def __str__(self):
        """Метод строкового представления"""
        return '{} {} {} {}'.format(self.number, self.type, self.max_capacity, self.comfort)

    def __repr__(self):
        """Метод представления"""
        return self.__str__()



    @staticmethod
    def max_price(room_prices):
        """Метод сортировки списка свободных комнат по убыванию цены"""
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
