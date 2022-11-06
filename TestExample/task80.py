# Вывести на экран ряд чисел 1001,  1004,  1007,  ... 1025.
a = 1001
lengt = 1026
step = 3
for i in range(a, lengt, step):
    print(i, end=", ")