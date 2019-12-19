# Определить, какое число в массиве встречается чаще всего.

import timeit
import cProfile
import random

s = """
def num_meets3(SIZE):
    array = [random.randint(0, 100) for _ in range(SIZE)]
    a = sorted([(i, array.count(i)) for i in set(array)], key=lambda t: t[1])[-1]
    

num_meets3(100)
"""

# print(timeit.timeit(s, number=100, globals=globals()))


# 0.0052433689997997135 num_meets3(10)
# 0.02452156199797173 num_meets3(50)
# 0.06594559700170066 num_meets3(100)

def num_meets3(SIZE):
    array = [random.randint(0, 100) for _ in range(SIZE)]
    a = sorted([(i, array.count(i)) for i in set(array)], key=lambda t: t[1])[-1]

# cProfile.run('num_meets3(100)')

# cProfile.run('num_meets3(10)')
# 79 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les_4_task_1b.py:21(num_meets3)

# cProfile.run('num_meets3(50)')
# 344 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 les_4_task_1b.py:21(num_meets3)

# cProfile.run('num_meets3(100)')
# 651 function calls in 0.003 seconds
# 1    0.000    0.000    0.002    0.002 les_4_task_1b.py:21(num_meets3)

# сложность данного алгоритма = O(Log n)

# Итог: алгоритм второго варианта лучше.
