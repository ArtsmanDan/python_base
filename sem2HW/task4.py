# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint


def generate_numbers(number):
    list_numbers = []
    number_positive = abs(number)
    number_negative = number_positive * -1
    for item in range(number_negative, number_positive + 1):
        list_numbers.append(item)
    return list_numbers


def generate_file(file, min, max, size):
    f = open(file, 'w')
    for item in range(size):
        f.write(str(randint(min, max)))
        f.write('\n')
    f.close()


def numbers_file2list(file):
    f = open(file, 'r')
    str_list = f.readlines()
    int_list = []
    for item in str_list:
        int_list.append(int(item))
    return int_list


def multiplication_numbers(list_numbers, position_numbers):
    result = 1
    for item in position_numbers:
        if 0 <= item < len(list_numbers):
            # print(list_numbers[item])
            result *= list_numbers[item]
    return result


position_list_size = 5
start_position = 0
file_name = 'file.txt'
n = int(input('Введите число: '))
list = generate_numbers(n)
print('список', list)
generate_file(file_name, start_position, len(list)-1, position_list_size)
position_list = numbers_file2list(file_name)
print('список позиций', position_list)
print('произведение = ', multiplication_numbers(list, position_list))
