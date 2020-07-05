from calendar import monthrange


class Date:

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return f"Day: {self._day}; Month: {self._month}; Year: {self._year}"

    @classmethod
    def extract_date(cls, date):
        day, month, year = map(int, date.split('-'))
        if cls.validate_date(day, month, year):
            return cls(day, month, year)
        else:
            print("Error! Fake date!")
            return None

    @staticmethod
    def validate_date(day, month, year):
        return not ((year < 1) or (month < 1 or month > 12) or (day < 1 or day > monthrange(year, month)[1]))


date_1 = "01-01-1999"
Date_1 = Date.extract_date(date_1)
print(Date_1)

date_2 = "38-01-1999"
Date_2 = Date.extract_date(date_2)
print(Date_2)
