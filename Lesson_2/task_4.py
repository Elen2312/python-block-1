# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
# первые 10 букв в слове.

user_data = list(input('Введите несколько слов через пробел: ').split())

for i, v in enumerate(user_data, 1):
    print(f'{i}) {v[:10]}')