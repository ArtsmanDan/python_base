# Семинар 1
# Задача 1.
# Написать программу, которая принимает на вход два целых числа и проверяет, является ли одно число квадратом другого.
# Примеры
# •	5, 25 -> да
# •	4,16->да
# •	25, 5 -> да
# •	8,9 -> нет

def find_min_max(num1, num2):
    if num1 < num2:
        return num1, num2
    else:
        return num2, num1


def is_square_number(num1, num2):
    result = False
    min_value, max_value = find_min_max(num1, num2)
    if min_value * min_value == max_value: result = True
    return result


num1 = 26
num2 = 5
print(num1, ", ", num2, "->", is_square_number(num1, num2))