# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы метод
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.

class Cell:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return str(self.count)

    def __add__(self, other):
        return Cell(abs(self.count + other.count))

    def __sub__(self, other):
        return Cell(abs(self.count - other.count))

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, row):
        while self.count > 0:
            for i in range(1, row+1):
                print('*',end='')
                self.count -= 1
                if self.count <= 0:
                    break
            print('\n')


c1 = Cell(8)
c2 = Cell(5)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

c1.make_order(4)
c2.make_order(3)