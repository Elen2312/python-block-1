# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

season_dict = {'зима': (1, 2, 12),
               'весна': (3, 4, 5),
               'лето': (6, 7, 8),
               'осень': (9, 10, 11)}
season_list = ['зима', 'весна', 'лето', 'осень', 'зима']
user_data = int(input('Введите номер месяца: '))

for key in season_dict.keys():
    if user_data in season_dict[key]:
        print(f'dict: {key}')
        break
    else:
        print('dict: error')
        break

if 1 <= user_data <= 12:
    month = season_list[user_data//3]
    print(f'list: {month}')
else:
    print('list: error')

