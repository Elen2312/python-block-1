# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат
from random import randrange


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        direction = randrange(1, 3)
        if direction == 1:
            print(f'Машина повернула влево')
        else:
            print(f'Машина повернула вправо')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости, больше 60')
        else:
            super().show_speed()


class SportCar(Car):
    def show_speed(self):
        if self.speed > 100:
            print(f'Превышение скорости, больше 100')
        else:
            super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости, больше 40')
        else:
            super().show_speed()


class PoliceCar(Car):
    # не смогла понять как реализовать эту идею
    def police(self):
        if not self.is_police:
            print('Это полицейская машина')
        else:
            print('Это не полицейская машина')



bmw = SportCar(120, 'blue', 'BMW', False)
kia = TownCar(70, 'white', 'KIA', False)
audi = WorkCar(50, 'black', 'Audi', True)
ford = PoliceCar(110, 'green', 'Ford', True)

bmw.show_speed()
kia.show_speed()
audi.show_speed()
ford.show_speed()

bmw.go()
kia.go()
audi.go()
ford.go()

bmw.stop()
kia.stop()
audi.stop()
ford.stop()

bmw.turn()
kia.turn()
audi.turn()
ford.turn()
