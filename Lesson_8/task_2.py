# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


data = input('Введите делитель: ')
try:
    number = int(data)
    if number == 0:
        raise DivisionZero('На ноль делить нельзя')
    else:
        print(f'10 / {number} = {10/number}')
except DivisionZero as err:
    print(err)
