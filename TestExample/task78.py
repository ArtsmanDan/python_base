# Вывести на экран фигуру из звездочек:
# *******
# *******
# *******
# *******
# # (квадрат из n строк, в каждой строке n звездочек)

n = 5


for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
