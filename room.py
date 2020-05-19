class Room:
    """Class of rooms."""
    breakfast = 280.0
    half_board = 1000.0

    lost_income = 0
    income = 0

    type_of_room = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    comfort_degree = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}

    def __init__(self, number, type, max_capacity, comfort):
        """Method of initialization."""
        self.number = number
        self.type = type
        if isinstance(max_capacity, str):
            self.max_capacity = int(max_capacity)
        else:
            self.max_capacity = max_capacity
        self.comfort = comfort
        self.booked_date = set()
        self.price = Room.type_of_room[self.type] * Room.comfort_degree[self.comfort]

    def __str__(self):
        """Method of string representation."""
        return 'номер {} {} {}'.format(self.number, self.type, self.comfort)

    def __repr__(self):
        """Method of representation."""
        return self.__str__()

    def isfreeroom(self, dates):
        """Method of determining whether a room is available."""
        if dates & self.booked_date == set():
            return True
        else:
            return False

    @staticmethod
    def max_price(room_prices):
        """Method of downwards sorting."""
        for i in range(len(room_prices)):
            for j in range(i, len(room_prices) - 1):
                if room_prices[j][0] < room_prices[j + 1][0]:
                    room_prices[j], room_prices[j + 1] = room_prices[j + 1], room_prices[j]
        return room_prices

    @staticmethod
    def min_capacity(lst_rooms):
        """Method of finding room with the lowest capacity."""
        rooms_capacity = []
        for room in lst_rooms:
            rooms_capacity.append([room.max_capacity, room])
        rooms_capacity.sort(key=lambda i: i[0])
        min_capacity = rooms_capacity[0][0]
        return min_capacity

    @staticmethod
    def lst_room_price(lst_rooms, min_capacity):
        """Method of maling the list of available rooms with their prices."""
        room_price = []
        for room in lst_rooms:
            if room.max_capacity == min_capacity:
                room_price.append([room.price, room])
        return room_price
