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


num = input('Введите число:')
print(f'{num} -> {sum_digits(num)}')
