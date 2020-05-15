class Client:
    def __init__(self, last_name, first_name, patronymic,
                 capacity, money, start_date, count_days):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.capacity = capacity
        self.money = money
        self.start_date = start_date
        self.count_days = count_days

    def __str__(self):
        s = self.last_name + ' '
        s += self.first_name + ' '
        s += self.patronymic + ' '
        s += str(self.capacity) + ' '
        s += str(self.money) + ' '
        s += self.start_date + ' '
        s += str(self.count_days)
        return s

    def __repr__(self):
        return self.__str__()

    def dates(self):
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
                    month == '01'
                    year = str(int(year) + 1)
                else:
                    month = '{:02d}'.format(int(month) + 1)
            else:
                day = '{:02d}'.format(day)
            needed_dates.add(str(day + '.' + month + '.' + year))

        return needed_dates
