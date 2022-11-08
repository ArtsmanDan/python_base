# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math

n = int(input('Введите натуральное число N: '))


def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


print(primfacs(n))

for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        print(i)
        n //= i

if n != 1:
    print(n)
