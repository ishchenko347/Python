# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

import random

x = random.randint(0,1)
y = random.randint(0,1)
z = random.randint(0,1)

F = not (x or y or z)
K = not x and not y and not z

if F == K:
    print(f'При значениях x = {x}, y = {y}, z = {z} утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является True')
else:
    print(f'При значениях x = {x}, y = {y}, z = {z} утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z является False')


# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

x = int(input('Введите х - '))
y = int(input('Введите y - '))

if x > 0 and y > 0:
    print('Точки x и y лежат в I четверти координатной плоскости')
elif x < 0 and y > 0:
    print('Точки x и y лежат во II четверти координатной плоскости')
elif x < 0 and y < 0:
    print('Точки x и y лежат в III четверти координатной плоскости')
elif x > 0 and y < 0:
    print('Точки x и y лежат в IV четверти координатной плоскости')
elif x == 0 and y > 0 or y < 0:
    print('Точки x и y лежат на оси y')
elif y == 0 and x > 0 or x < 0:
    print('Точки x и y лежат на оси x')

# 15. Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды 

sec = 15379

d = sec // 86400
sec = sec - (d * 86400)
h = sec // 3600
sec = sec - (h * 3600)
m = sec // 60
sec = sec - (m * 60)

print(f'{d}d : {h}h : {m}m : {sec}s')

# 16. Написать программу проверки, является ли строка палиндромом

word = 'anna'

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")