class MyComplexNumber:
    def __init__(self, real, complex):
        self._real = real
        self._complex = complex

    def __str__(self):
        return f"(r: {self._real}; c: {self._complex})"

    def __add__(self, other):
        return MyComplexNumber(self._real + other._real,
                               self._complex + other._complex)

    def __mul__(self, other):
        return MyComplexNumber(self._real * other._real - self._complex * other._complex,
                               self._real * other._complex + self._complex * other._real)


complex_1 = MyComplexNumber(1, 1)
complex_2 = MyComplexNumber(2, -2)

print(complex_1)
print(complex_2)
print(f"{complex_1} + {complex_2} = {complex_1 + complex_2}")
print(f"{complex_1} * {complex_2} = {complex_1 * complex_2}")
