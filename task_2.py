# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк

user_time = int(input('Введите время в секундах: '))

max_width = 2
hour = user_time//3600
minutes = (user_time - hour * 3600)//60
seconds = user_time - hour * 3600 - minutes * 60
print(f'{user_time} секунд это {hour:0{max_width}}:{minutes:0{max_width}}:{seconds:0{max_width}}')
