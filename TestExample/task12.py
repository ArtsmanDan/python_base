# Вычислите значение выражения ex−2+|sin(x)|−x4⋅cos1x при x=3.6 Ответ: -156.1276
import math

x = 3.6

y = math.exp(x - 2) + abs(math.sin(x)) - x ** 4 * math.cos(1 / x)
print(y)
