# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.
from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter

    def __str__(self):
        return str(self.parameter)

    def __add__(self, other):
        return self.parameter + other.parameter

    @abstractmethod
    def total_tissue(self):
        pass


class Coat(Clothes):
    @property
    def total_tissue(self):
        return round((self.parameter / 6.5 + 0.5), 2)


class Suit(Clothes):
    @property
    def total_tissue(self):
        return round((self.parameter * 2 + 0.3), 2)


coat = Coat(42)
suit = Suit(1.7)
print(f'Расход ткани для пальто размера {coat} - {coat.total_tissue}')
print(f'Расход ткани для костюма на рост {suit} - {suit.total_tissue}')
total = coat.total_tissue + suit.total_tissue
print(f'Общий расход ткани - {total}')
