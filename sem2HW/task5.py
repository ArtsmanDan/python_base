# Реализуйте алгоритм перемешивания списка.
import random


def mix_list(array):
    list_new = array[:]
    list_length = len(list_new)
    for i in range(list_length):
        index_random = random.randint(0, list_length - 1)
        temp = list_new[i]
        list_new[i] = list_new[index_random]
        list_new[index_random] = temp
    return list_new


list_numbers = [3, 6, 9, 12, 15, 18]
list_numbers_new = mix_list(list_numbers)
print(list_numbers)
print(list_numbers_new)
