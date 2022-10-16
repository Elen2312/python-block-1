# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def user(**kwargs):
    return kwargs


name = input('Введите имя: ').title()
surname = input('Введите фамилию: ').title()
year = int(input('Введите год рождения: '))
city = input('Введите город проживания: ').title()
email = input('Введите email: ')
telephone = int(input('Введите номер телефона: '))

print(user(surname=surname, name=name, year=year, city=city, email=email, telephone=telephone))
