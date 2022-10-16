# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль

def division(x, y):
    """
    Функция деления.

    :param x: делимое
    :param y: делитель

    """
    print(f'{x}/{y} = {x / y}')


try:
    x_user_data = int(input('Введите первое число: '))
    y_user_data = int(input('Введите второе число: '))
    division(x_user_data, y_user_data)
except ZeroDivisionError:
    print("На 0 делить нельзя!")


