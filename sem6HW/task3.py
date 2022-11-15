# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fractional_part_to_int(list_nums):
    return [f % 1 for f in list_nums]

def min_max(list_nums):
    min = list_nums[0]
    max = list_nums[0]
    for item in list_nums:
        if min > item: min = item
        if max < item: max = item
    return min, max


list_nums = [1.1, 1.2, 3.1, 5, 10.01]
print(list_nums)
# list_fractional_part = fractional_part_to_int(list_nums)
list_fractional_part = list(map(lambda x: x % 1, list_nums))
print(list_fractional_part)
min, max = min_max(list_fractional_part)
print(f"минимальное число = {min}, максимальное число = {max}")
print(max - min)
