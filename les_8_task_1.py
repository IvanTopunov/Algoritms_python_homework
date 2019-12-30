# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9


import hashlib
import collections


def hash_count(your_word):
    word = str(your_word)

    word_hash = hashlib.sha1(bytes(word, 'utf-8')).hexdigest()

    hash_list = {}
    collections.OrderedDict(hash_list)

    for i in range(len(word)):
        letter = ''
        for j in word[i:]:
            letter += j
            hash_letter = hashlib.sha1(bytes(letter, 'utf-8')).hexdigest()

            if hash_letter != word_hash and hash_letter not in hash_list:
                hash_list[letter] = hash_letter

    return hash_list


while True:
    my_word = input('Введите строку, количество хешированных подстрок которой вы хотите найти: ')
    if my_word == '':
        print('Вы ничего не ввели, попробуйте еще раз!')
    else:
        break

my_word_hash = hash_count(my_word)
print(f'\nВ вашей строке {my_word} содержится {len(my_word_hash)} хешированных подстрок:')

for key, value in my_word_hash.items():
    print('\t', f'{key} - {value}')
