# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def find_negative_position(nums):
    nums_negative = []
    for item in range(1, len(nums), 2):
        nums_negative.append(nums[item])
    return nums_negative


def sum_nums(list_nums):
    sum = 0
    for num in list_nums:
        sum += num
    return sum


nums = [2, 3, 5, 9, 3]
list_nums = find_negative_position(nums)
print(list_nums)
print(sum(list_nums))
