# Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки)
# вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.


# ОС: Linux Ubuntu 18.04.3 LTS 64-бит. Интерпретатор Python: Python 3.6.9

# Задача 1 из 5 урока:
# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import random
import collections
import sys


def test_size(array, reqursion_level=1):
    global_size = sys.getsizeof(array)

    print('\t' * reqursion_level, f'Объект {array}')
    print('\t' * reqursion_level, f'типа {array.__class__}')
    print('\t' * reqursion_level, f'имеет размерность = {global_size}')

    if hasattr(array, '__iter__'):
        if array.__class__ == collections.OrderedDict or array.__class__ == dict:
            for value in array:
                global_size += test_size(value, reqursion_level + 1)
                global_size += test_size(array[value], reqursion_level + 2)

        elif not isinstance(array, str):
            for i in array:
                global_size += test_size(i, reqursion_level + 1)

    return global_size


# 1 вариант
COUNT_COMPANY = 4
QUARTES = 4
company_dict = {i: int(sum([random.randint(1000, 1000000) for _ in range(4)]) / QUARTES)
                for i in ('Coca-Cola', 'Mirinda', 'Sprite', 'Fanta')}
print(f'Общий размер словаря company_dict = {test_size(company_dict)}\n')

# Итог: размер класса 'dict' = 248 байт
# размер словаря с 4 компаниями и их средней прибылью за 4 квартала = 583 байт
# Для решения данной задачи нам потребуется 2 дополнительных перебора всех переменных в словаре и
# сравнение их со средней стоимостью для вывода сначала копаний с прибылью больше средней, а затем с меньше средней.

print("*" * 50)

# 2 вариант
COUNT_COMPANY = 4
QUARTES = 4
company_dict = {i: int(sum([random.randint(1000, 1000000) for _ in range(4)]) / QUARTES)
                for i in ('Coca-Cola', 'Mirinda', 'Sprite', 'Fanta')}
company_dict = collections.OrderedDict(sorted(company_dict.items(), key=lambda x: x[1]))

print(f'Общий размер OrderedDict company_dict = {test_size(company_dict)}\n')

# Итог: размер класса 'collections.OrderedDict' = 504 байт,
# размер словаря с 4 компаниями и их средней прибылью за 4 квартала = 839 байт
# Для решения данной задачи нам так же потребуется 2 дополнительных перебора всех переменных в словаре и
# сравнение их со средней стоимостью для вывода сначала копаний с прибылью больше средней, а затем с меньше средней.

print("*" * 50)

# 3 вариант
COUNT_COMPANY = 4
QUARTES = 4
Company = collections.namedtuple('Company', ['name', 'quartes', 'profit'])
all_company = set()

for i in ('Coca-Cola', 'Mirinda', 'Sprite', 'Fanta'):
    quartes = []
    profit = 0
for j in range(QUARTES):
    quartes.append(random.randint(1000, 1000000))
    profit += quartes[j]

comp = Company(name=i, quartes=tuple(quartes), profit=profit)
all_company.add(comp)

print(f'Общий размер множества all_company = {test_size(all_company)}')

# Итог: размер класса 'set' переменной all_company = 232 байта,
# внутри получается 4 объекта классна __main__.Company с размером 80 байта
# размер словаря с 4 компаниями и их прибылью за 4 квартала и средней прибылью = 594 байта

# Вывод: Самый выгодный тип хранения данных для решения данной задачи из 3 представленных способов,
# это использование стандартного словаря, он, заполненный, потребляет наименьшее количество памяти,
# а имено - 583 байта.
