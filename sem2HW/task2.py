# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factor(n):
    fact = 1
    print(f'пусть N = {n}, тогда [', end=" ")
    for i in range(n):
        i = i + 1
        fact = fact * i
        print(fact, end=" ")
    print(']')


num = int(input('Введите число: '))
factor(num)