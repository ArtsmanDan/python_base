# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
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


# получение степени многочлена
def get_deg(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


# получение коэффицента члена многочлена
def get_coef(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if get_deg(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  # степень
    ii = l - 1  # индекс
    while ii >= 0:
        if get_deg(st[ii]) != -1 and get_deg(st[ii]) == i:
            lst.append(get_coef(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


# создание двух файлов
min = 0
max = 100
k1 = int(input("Введите натуральную степень многочлена k1 = "))
k2 = int(input("Введите натуральную степень многочлена k2 = "))
list1 = fill_list_nums(min, max + 1, k1 + 1)
list2 = fill_list_nums(min, max + 1, k2 + 1)

pos_not_zero = get_first_position_not_zero(list1)
if len(list1) == 0 or pos_not_zero == -1:
    print('Многочлен невозможно создать len = 0 or pos_not_zero == -1')
    exit()
polynomial1 = get_polynomial(list1)
print(polynomial1)
with open('polynomial1.txt', 'w') as data:
    data.write(polynomial1)

pos_not_zero = get_first_position_not_zero(list2)
if len(list2) == 0 or pos_not_zero == -1:
    print('Многочлен невозможно создать len = 0 or pos_not_zero == -1')
    exit()
polynomial2 = get_polynomial(list2)
print(polynomial2)
with open('polynomial2.txt', 'w') as data:
    data.write(polynomial2)

# нахождение суммы многочлена

with open('polynomial1.txt', 'r') as data:
    polynomial1 = data.readlines()
with open('polynomial2.txt', 'r') as data:
    polynomial2 = data.readlines()
print(f"Первый многочлен {polynomial1}")
print(f"Второй многочлен {polynomial2}")
lst1 = calc_mn(polynomial1)
lst2 = calc_mn(polynomial2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
polynomial_sum = get_polynomial(lst_new)
with open('polynomial_sum.txt', 'w') as data:
    data.write(polynomial_sum)
with open('polynomial_sum.txt', 'r') as data:
    polynomial_sum = data.readlines()
print(f"Результирующий многочлен {polynomial_sum}")
