# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе

my_list = [12, 'word', True, 1.7, None, [2, 6]]

for i in range(len(my_list)):
    print(type(my_list[i]))