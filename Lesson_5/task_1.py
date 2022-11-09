# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка

my_f = open('text_1.txt', 'w', encoding='utf-8')
data = input('Введите текст: ')
while data:
    my_f.writelines(f'{data}\n')
    data = input('Введите текст: ')
    if not data:
        break
my_f.close()

my_f = open('text_1.txt', 'r', encoding='utf-8')
print(my_f.readlines())
my_f.close()
