# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math


def get_distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1 = 3
y1 = 6
x2 = 2
y2 = 1
distance = get_distance_2d(x1, y1, x2, y2)
print(f'A ({x1},{y1}); B ({x2},{y2}) -> {round(distance, 3)}')