import math  # Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
a = 2
a1 = 3
b = 6
b1 = 1

x = math.sqrt((a1 - a) ** 2 + (b1 - b) ** 2)
print(x)


# ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5

