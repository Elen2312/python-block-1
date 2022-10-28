# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text_3.txt', 'r', encoding='utf-8') as my_f:
    salary = []
    staff = []
    my_list = my_f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000.00:
            staff.append(i[0])
        salary.append(i[1])
    print(f'Оклад меньше 20 000 - {staff}, средний оклад {round(sum(map(float, salary)) / len(salary), 2)}')
