# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

# Вариант 1
from transliterate import translit

with open('text_4.txt', 'r', encoding='utf-8') as my_f:
    with open('text_4_rus.txt', 'w', encoding='utf-8') as rus:
        data = my_f.read()
        data_rus = translit(data, 'ru')
        print(data_rus, file=rus)

# Вариант 2
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_file = []
with open('text_4.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.split(' ', 1)
        rus_file.append(rus[i[0]] + ' ' + i[1])
    print(rus_file)

with open('text_4_rus_v2.txt', 'w', encoding='utf-8') as file_r:
    file_r.writelines(rus_file)
