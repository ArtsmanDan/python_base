# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math


def pow_twins(list_nums):
    list_twins = []
    for item in range(math.ceil(len(list_nums) / 2)):
        twins = list_nums[item] * list_nums[-1 - item]
        # print(list_nums[item], list_nums[-1 - item])
        list_twins.append(twins)
    return list_twins


list_nums = [2, 3, 4, 5, 6]
list_nums2 = [2, 3, 5, 6]
list_twins = pow_twins(list_nums2)
print(list_twins)
