# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = array[0]
max_num = 1
for i in range(SIZE - 1):
    current = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            current += 1
    if current > max_num:
        max_num = current
        num = array[i]

if max_num > 1:
    print(f'В этом массиве {max_num} раз встречается число {num}')
else:
    print('Нет повторяющихся чисел в этом массиве')
