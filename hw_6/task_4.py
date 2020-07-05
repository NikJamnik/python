class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car has started!")

    def stop(self):
        print("Car has stopped!")

    def turn(self, direction):
        print(f"Car has turned {direction}!")

    def show_speed(self):
        print(f"Car speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Warning! High speed!")
        else:
            print(f"Town car speed is {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Warning! High speed!")
        else:
            print(f"Work car speed is {self.speed}")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'black', 'Volvo', False)
town_car.show_speed()
town_car.speed = 50
town_car.show_speed()

work_car = WorkCar(50, 'red', 'Mercedes', False)
work_car.show_speed()
work_car.speed = 35
work_car.show_speed()
