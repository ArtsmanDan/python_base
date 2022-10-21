# Задача 5.
# Напишите программу, которая будет принимать
# на вход дробь и показывать первую цифру дробной части числа.
# Примеры
# 6.78 -> 7
# 5 -> нет
# 0.34 -> 3
import math

num = 5.54
drob = abs(num * 10) % 10
result = math.trunc(drob)
if result != 0:
    print(num, '->', result)
else:
    print(num, '-> нет')
