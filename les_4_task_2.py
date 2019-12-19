# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile
import random


# Первый — с помощью алгоритма «Решето Эратосфена».


def num_erat(num):
    n = 10000
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(res[num - 1])


s = """
def num_erat(num):
    n = 10000
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    
        
num_erat(10)
"""


# cProfile.run('num_erat(1000)')
# print(timeit.timeit(s, number=100))

# 0.5825039429983008 num_erat(10)
# 0.5578930049960036 num_erat(100)
# 0.6273138429969549 num_erat(1000)

# num_erat(10)
# 1    0.005    0.005    0.006    0.006 les_4_task_2.py:14(num_erat)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:16(<listcomp>)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:26(<listcomp>)

# num_erat(100)
# 1    0.005    0.005    0.007    0.007 les_4_task_2.py:14(num_erat)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:16(<listcomp>)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:26(<listcomp>)

# num_erat(1000)
# 1    0.006    0.006    0.008    0.008 les_4_task_2.py:14(num_erat)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:16(<listcomp>)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:26(<listcomp>)


# Второй — без использования «Решета Эратосфена».


def no_erast(n):
    prime = []
    for i in range(2, 10000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    # print(f'{prime[n - 1]}')


s = """
def no_erast(n):
    prime = []
    for i in range(2, 10000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    

no_erast(1000)
"""

# cProfile.run('num_erat(1000)')
# print(timeit.timeit(s, number=100))


# 70.13930009400065 no_erast(10)
# 72.0242036990021 no_erast(100)
# 70.42112783099583 no_erast(1000)

# num_erat(10)
# 1    0.005    0.005    0.007    0.007 les_4_task_2.py:14(num_erat)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:16(<listcomp>)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:26(<listcomp>)

# num_erat(100)
# 1    0.007    0.007    0.008    0.008 les_4_task_2.py:14(num_erat)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:16(<listcomp>)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:26(<listcomp>)

# num_erat(1000)
# 1    0.005    0.005    0.007    0.007 les_4_task_2.py:14(num_erat)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:16(<listcomp>)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:26(<listcomp>)
