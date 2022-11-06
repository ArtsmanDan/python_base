# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonachi(n):
    list_nums = []
    a, step = 1, 1
    for i in range(n):
        list_nums.append(a)
        a, step = step, a + step
    a, step = 0, 1
    for i in range(n + 1):
        list_nums.insert(0, a)
        a, step = step, a - step
    return list_nums


num = int(input('Введите число: '))
f_nums = fibonachi(num)
print(f_nums)
