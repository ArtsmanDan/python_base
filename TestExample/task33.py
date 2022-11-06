# Вычислите x−y√−−−−−−√, если x и y вводит пользователь. Перед вычислением выполнить проверку на существование квадратных корней.

import math

x = int(input('Введите число: '))

y = int(input('Введите число: '))

if x > 0 and y > 0:
    num = 0
    y = math.sqrt(y)
    num = x - y
    num = math.sqrt(num)
    print(num)




