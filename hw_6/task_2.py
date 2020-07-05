class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_weight(self, layers):
        return (self._length * self._width * 25 * layers) / 1000


road_1 = Road(20, 5000)
print(f"Road_1 weight: {road_1.count_weight(5)} tones")
