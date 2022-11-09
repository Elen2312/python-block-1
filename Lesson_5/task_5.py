# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as my_f:
    data = [randint(1, 20) for i in range(10)]
    my_f.writelines(str(data))
    my_f.seek(0)
    print(my_f.read())
    print(f'Сумма чисел - {sum(map(int, data))}')
