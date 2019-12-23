# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

count = int(input('Введите кол-во компаний: '))

comp = collections.defaultdict(list)

for i in range(count):
    name = input(f'Введите имя {i + 1} компании: ')
    profit = [(int(input(f'Введите прибыль за {j + 1} квартал: '))) for j in range(4)]
    comp[name] = sum(profit)

avg_profit = int(sum(comp.values()) / count)
print(f'Средняя прибыль (за год для всех предприятий) равна: {avg_profit}')

for i in comp:
    if comp[i] < avg_profit:
        print(f'Компания "{i}" имеет прибыль ниже средней и она равна: ({comp[i]})')
    elif comp[i] > avg_profit:
        print(f'Компания "{i}" имеет прибыль выше средней и она равна: ({comp[i]})')
