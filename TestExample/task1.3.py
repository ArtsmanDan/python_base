# Напишите программу, которая принимает на вход координаты точки (X и Y), при чём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = - 34
y = 30

if x > 0 and y < 0:
    print(f"{x} ; {y} -> 4")
if x > 0 and y > 0:
    print(f"{x} ; {y} -> 1")
if x < 0 and y < 0:
    print(f"{x} ; {y} -> 3")
if x < 0 and y > 0:
    print(f"{x} ; {y} -> 2")