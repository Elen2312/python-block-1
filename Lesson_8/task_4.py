# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class Stock:
    pass


class OfficeEquipment:
    vat = 1.13

    def __init__(self, eq_type, model, color, price):
        self.type = eq_type
        self.model = model
        self.color = color
        self.price = price

    @property
    def total_price(self):
        return f'Стоимость с НДС - {round(self.price * self.vat)}'

    def __str__(self):
        return f'{self.type} {self.model} color: {self.color}'


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Сканер', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Ксерокс', *args)


p1 = Printer("Epson", "black", 15000)
print(p1)
print(p1.total_price)
s1 = Scanner("Canon", "white", 20000)
print(s1)
print(s1.total_price)
x1 = Xerox("Xerox ", "gray", 35000)
print(x1)
print(x1.total_price)