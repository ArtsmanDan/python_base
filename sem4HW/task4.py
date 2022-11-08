# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def fill_list_nums(a, b, len):
    list_nums = []
    for item in range(len):
        list_nums.append(random.randint(a, b))
    return list_nums


def get_first_position_not_zero(list):
    result = -1
    for item in range(len(list) - 1, -1, -1):
        if list[item] != 0:
            result = item
            break
    return result


def isZero(list, pos):
    result = False
    if list[pos] == 0:
        result = True
    return result


def generate_x(coef, deg):
    coef = str(abs(coef))
    deg = str(abs(deg))
    if coef == '0': return ''
    # if coef == '1': coef = ''
    deg_out = 'x^' + deg
    if deg == '0': deg_out = ''
    if deg == '1': deg_out = 'x'
    return coef + deg_out


# def get_polynomial(list):
#     s = ''
#     j = get_first_position_not_zero(list)
#     s += generate_x(list[j], len(list) - j)
#     for k in range(len(list) - j, 0, -1):
#         x = generate_x(list[k - 1], k - 1)
#         print(list[k - 1], k - 1, x)
#         if x == '':
#             continue
#         s += ' + ' + x
#     print(s)

def get_polynomial(list):
    s = ''
    for i in range(len(list)):
        if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
            s += f'{list[i]}x^{len(list) - i - 1}'
            if list[i + 1] != 0:
                s += ' + '
        elif i == len(list) - 2 and list[i] != 0:
            s += f'{list[i]}x'
            if list[i + 1] != 0:
                s += ' + '
        elif i == len(list) - 1 and list[i] != 0:
            s += f'{list[i]} = 0'
        elif i == len(list) - 1 and list[i] == 0:
            s += ' = 0'
    return s


min = 0
max = 100
k = 5
k = int(input("Введите натуральную степень многочлена k = "))
list = fill_list_nums(min, max + 1, k + 1)
# list = [0,0,0,0,0,0]
# list = [2, 6, 7, 8, 1, 0]
# list = []
pos_not_zero = get_first_position_not_zero(list)
if len(list) == 0 or pos_not_zero == -1:
    print('Многочлен невозможно создать len = 0 or pos_not_zero == -1')
    exit()
polynomial = get_polynomial(list)
print(polynomial)
with open('polynomial.txt', 'w') as data:
    data.write(polynomial)
