# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

my_f = open('text_2.txt', 'r', encoding='utf-8')

data = my_f.readlines()
print(f'Количество строк в файле - {len(data)}')

for i in range(len(data)):
    print(f'Количество символов {i + 1}-ой строки {len(data[i])}')

my_f = open('text_2.txt', 'r', encoding='utf-8')
words = my_f.read().split()
print(f'Общее количество слов - {len(words)}')
my_f.close()


