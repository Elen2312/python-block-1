# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
# завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится.


from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

n = 0
my_list = list(input('Введите элементы списка: ').split())
for el in cycle(my_list):
    if n > 10:
        break
    else:
        print(f'{n}) {el}')
    n += 1
