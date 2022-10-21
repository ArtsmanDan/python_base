# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# •	1,4, 8, 7, 5->8
# •	78, 55, 36. 90, 2 -> 90

def find_max_value(list_numbers):
    max_value_f = list_numbers[0]
    for item in list_numbers:
        if max_value_f < item: max_value_f = item
    return max_value_f


list_numbers1 = [1, 4, 8, 7, 5]
list_numbers2 = [78, 55, 36, 90, 2]
print(list_numbers1, "->", find_max_value(list_numbers1))
