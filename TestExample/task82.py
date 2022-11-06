# Выведите на экран числа 1.2, 1.4, 1.6, ..., 2.8.


a1 = 1
a2 = 2
b1 = 2
b2 = 8
step = 2
print(f'{a1}.{a2},', end=" ")
while (True):
    a2 = a2 + step
    if a2 >= 10:
        a1 += 1
        a2 = 0
    print(f'{a1}.{a2},', end=" ")
    if a1 == b1 and a2 == b2:
        break


