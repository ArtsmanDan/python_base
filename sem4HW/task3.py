# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.
import random
from collections import Counter


def fill_list_nums(a, b, len):
    list_nums = []
    for item in range(len):
        list_nums.append(random.randint(a, b))
    return list_nums


def unique_values_list(user_list) -> list:
    new_list = [user_list[0]]
    for i in range(1, len(user_list)):
        for j in range(len(new_list)):
            if user_list[i] == new_list[j]:
                break
            elif j == len(new_list) - 1:
                new_list.append(user_list[i])
    return new_list


def delete_copy_nums(list_nums):
    list_result = []
    c = Counter(list_nums)
    for item in list_nums:
        if c[item] == 1:
            list_result.append(item)
    return list_result


nums = [44, 33, 80, 3, 15, 74, 87, 15, 20, 21, 5, 86, 32, 93, 40, 72, 15, 2, 40, 8, 44, 3, 33]
print(nums, "исходный")
list_nums = fill_list_nums(0, 100, 20)
list_del_copy_num = delete_copy_nums(nums)
print(list_del_copy_num, "убраны повторяющиеся")
print(unique_values_list(nums), "убраны копии")
