# Задача 3.
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# 5-> -5, -4, -3, -2,-1,0, 1,2, 3, 4,5

def generate_numbers(number):
    number_positive = abs(number)
    number_negative = number_positive * -1
    for item in range(number_negative, number_positive + 1):
        print(item, ',', end='')


generate_numbers(-8)
