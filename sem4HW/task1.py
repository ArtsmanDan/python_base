# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
from decimal import getcontext, Decimal

print(f"Число Пи = {math.pi}")

d = int(input('Введите число точности вычисления числа ПИ: '))

pi = sum(1 / 16 ** x * (4 / (8 * x + 1) - 2 / (8 * x + 4) - 1 / (8 * x + 5) - 1 / (8 * x + 6)) for x in range(d))
print(pi)


def pi_decimal(d):
    getcontext().prec += d  # extra digits for intermediate steps
    three = Decimal(3)  # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s  # unary plus applies the new precision


print(pi_decimal(d))
