# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов

def my_func(x, y, z):
    if x >= z and y >= z:
        return x + y
    elif y <= x <= z:
        return x + z
    else:
        return y + z


print(f'Результат - {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')
