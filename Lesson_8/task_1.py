# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def split_data(cls, day_month_year):
        new_data = []
        for i in day_month_year.split('-'):
            new_data.append(i)
        return int(new_data[0]), int(new_data[1]), int(new_data[2])

    @staticmethod
    def check_data(day, month, year):
        if (1 <= day <= 31) & (1 <= month <= 12) & (1990 <= year <= 2022):
            print(day, month, year)
        else:
            print(f'Некорректная дата')

    def __str__(self):
        return f'Текущая дата {Data.split_data(self.day_month_year)}'


total = Data('01 - 11 - 2022')
print(total)
print(Data.split_data('14-05-2020'))
Data.check_data(81, 12, 1990)
Data.check_data(11, 11, 2019)
