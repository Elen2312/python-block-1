# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
# прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчёте на одного сотрудника.

revenue = int(input('Введите размер выручки: '))
costs = int(input('Введите размер издержек: '))
profit = revenue - costs
rentabel = (revenue // costs) / revenue

if revenue > costs:
    print(f'Фирма получила прибыль {profit}, рентабельность равна {rentabel}')
    number_of_staff = int(input('Введите численность сотрудников: '))
    profit_per_employee = profit / number_of_staff
    print(f'Прибыль фирмы в расчёте на одного сотрудника - {profit_per_employee}')
else:
    print(f'Фирма работает в убыток {profit}')