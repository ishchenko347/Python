# 6. Реализовать алгоритм перемешивания списка. 

from random import randint, shuffle

list = []

for i in range(randint(5, 10)):
    list.append(randint(1, 10))
print(f'Исходный список {list}')

shuffle(list)
print(f'Перемешанный список {list}')


# 7. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

# Линейный конгруэнтный метод — один из методов генерации псевдослучайных чисел.

# x[i+1] = (a * x[i] + c) mod m

import math
import time

m = 32768
a = 23
c = 12345

def lin_rand(seed,size):
    if size == 1:
        return math.ceil(math.fmod(a * math.ceil(seed) + c, m))     # округление остатка от деления 

    r = [0 for i in range(size)]    # заполняет нулями список size-элементов
    r[0] = math.ceil(seed)          # нулевой элемент - округление времени

    for i in range(1, size):
        r[i] = math.ceil(math.fmod((a * r[i-1] + c), m))
    return r[1:size]

print(lin_rand(time.time(), 4))      