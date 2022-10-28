# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

profit = {}
aver_profit = {}
total_profit = 0
profit_aver = 0
i = 0
with open('text_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            total_profit += profit.setdefault(name)
            i += 1
    if i != 0:
        profit_aver = total_profit / i
        print(f'Прибыль средняя - {profit_aver}')
    else:
        print(f'Все работают в убыток')
    aver_profit = {'Прибыль средняя': round(profit_aver)}
    profit.update(aver_profit)
    print(f'Итог - {profit}')

with open('file_7.json', 'w', encoding='utf-8') as w_js:
    json.dump(profit, w_js)
