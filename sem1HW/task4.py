# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def print_points(plane):
    if plane == 1: print('1 -> x > 0 and y > 0')
    if plane == 2: print('2 -> x < 0 and y > 0')
    if plane == 3: print('3 -> x < 0 and y < 0')
    if plane == 4: print('4 -> x > 0 and y < 0')



plane1 = 1
plane2 = 2
plane3 = 3
plane4 = 4
print_points(plane1)
print_points(plane2)
print_points(plane3)
print_points(plane4)