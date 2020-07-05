class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position_1 = Position("Nikolay", "Jamgaryan", "Data scientist", 120000, 50000)
print(position_1.get_full_name())
print(position_1.get_total_income())

position_2 = Position("Egor", "Krinzh", "Singer", 1200000, 500000)
print(position_2.get_full_name())
print(position_2.get_total_income())
