# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

def sum_digits(user_num):
    sum_value = 0
    for digit in user_num:
        if digit.isdigit():
            sum_value += int(digit)
    return sum_value


def sum_list(list):
    sum = 0
    for x in list:
        sum += x
    return sum


num = input('Введите число:')
li = list(filter(lambda x: x.isdigit(), num))
print(li)
li = list(map(int, li))
print(li)
print(f'{num} -> {sum_digits(num)}')
print(f'{num} -> {sum(li)}')
