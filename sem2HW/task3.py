# Задайте список из n чисел
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
#
# - Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }

n = int(input('Введите число: '))


def seq(n):
    print(f'Для n = {n}:', end=' ')
    return [round((1 + 1 / x) ** x, 3) for x in range(1, n + 1)]


print(seq(n))
print(f'сумма = {sum(seq(n))}')
