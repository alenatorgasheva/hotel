from room import Room


class Client:
    """Class of hotel's client"""

    def __init__(self, last_name, first_name, middle_name,
                 capacity, money, start_date, count_days):
        """Method of initialization."""
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

        if isinstance(capacity, str):
            self.capacity = int(capacity)
        else:
            self.capacity = capacity

        if isinstance(money, str):
            self.money = int(money)
        else:
            self.money = money

        self.start_date = start_date

        if isinstance(count_days, str):
            self.count_days = int(count_days)
        else:
            self.count_days = count_days

    def __str__(self):
        """Method of string representation."""
        s = self.last_name + ' '
        s += self.first_name + ' '
        s += self.middle_name + ' '
        s += str(self.capacity) + ' '
        s += str(self.money) + ' '
        s += self.start_date + ' '
        s += str(self.count_days)
        return s

    def __repr__(self):
        """Method of representation."""
        return self.__str__()

    def dates(self):
        """Method of getting dates to book."""
        days_in_month = {'01': 31, '02': 28, '03': 31, '04': 30,
                         '05': 31, '06': 30, '07': 31, '08': 31,
                         '09': 30, '10': 31, '11': 30, '12': 31}

        day, month, year = self.start_date.split('.')
        day = '{:02d}'.format(int(day) - 1)
        needed_dates = set()
        for _ in range(self.count_days):
            day = int(day) + 1
            if days_in_month[month] < day:
                day = '01'
                if month == '12':
                    month = '01'
                    year = str(int(year) + 1)
                else:
                    month = '{:02d}'.format(int(month) + 1)
            else:
                day = '{:02d}'.format(day)
            needed_dates.add(str(day + '.' + month + '.' + year))

        return needed_dates

    def calc_new_price(self, lst_rooms, min_capacity):
        """Method of calculating the most expensive kind of room reservation."""
        if self.capacity < min_capacity:
            for room in lst_rooms:
                room[0] = room[0] * 0.7
        for room in lst_rooms:
            if room[0] + Room.breakfast <= self.money:
                if room[0] + Room.half_board <= self.money:
                    room[0] = room[0] + Room.half_board
                else:
                    room[0] = room[0] + Room.breakfast
