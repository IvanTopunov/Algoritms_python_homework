# Определить, какое число в массиве встречается чаще всего.

import timeit
import cProfile
import random

# SIZE = 20
# MIN_ITEM = 0
# MAX_ITEM = 100
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)


# ваниант 2

s = """
def num_meets2(SIZE):
    array = [random.randint(0, 100) for _ in range(SIZE)]
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return 'Все элементы уникальны'
    
num_meets2(100)
"""


# print(timeit.timeit(s, number=100, globals=globals()))


# 0.005935612000030233 num_meets2(10)
# 0.019260032000602223 num_meets2(50)
# 0.036716357000841526 num_meets2(100)


def num_meets2(SIZE):
    array = [random.randint(0, 100) for _ in range(SIZE)]
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return 'Все элементы уникальны'

# cProfile.run('num_meets2(100)')

# cProfile.run('num_meets2(10)')
# 58 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les_4_task_1a.py:48(num_meets2)
# 1    0.000    0.000    0.000    0.000 les_4_task_1a.py:49(<listcomp>)

# cProfile.run('num_meets2(50)')
# 269 function calls in 0.010 seconds
# 1    0.000    0.000    0.009    0.009 les_4_task_1a.py:48(num_meets2)
# 1    0.008    0.008    0.009    0.009 les_4_task_1a.py:49(<listcomp>)

# cProfile.run('num_meets2(100)')
# 531 function calls in 0.005 seconds
# 1    0.000    0.000    0.005    0.005 les_4_task_1a.py:48(num_meets2)
# 1    0.000    0.000    0.005    0.005 les_4_task_1a.py:49(<listcomp>)

# сложность данного алгоритма = O(n)
