# Определить, какое число в массиве встречается чаще всего.

import timeit
import cProfile
import random

# SIZE = 20
# MIN_ITEM = 0
# MAX_ITEM = 100
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)


# вариант 1

s = """
def num_meets(SIZE):
    array = [random.randint(0, 100) for _ in range(SIZE)]
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    if frequency > 1:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return f'Все элементы уникальны'
        
num_meets(100)
"""


# print(timeit.timeit(s, number=100, globals=globals()))

# 0.0063491529999737395 num_meets(10)
# 0.041928152000764385 num_meets(50)
# 0.11103376299979573 num_meets(100)


def num_meets(SIZE):
    array = [random.randint(0, 100) for _ in range(SIZE)]
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    if frequency > 1:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return f'Все элементы уникальны'

# cProfile.run('num_meets(100)')

# cProfile.run('num_meets(10)')
# 70 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:45(num_meets)
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:46(<listcomp>)

# cProfile.run('num_meets(50)')
# 323 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 les_4_task_1.py:45(num_meets)
# 1    0.000    0.000    0.001    0.001 les_4_task_1.py:46(<listcomp>)

# cProfile.run('num_meets(100)')
# 636 function calls in 0.003 seconds
# 1    0.001    0.001    0.003    0.003 les_4_task_1.py:45(num_meets)
# 1    0.000    0.000    0.002    0.002 les_4_task_1.py:46(<listcomp>)

# сложность данного алгоритма = O(n^2)
