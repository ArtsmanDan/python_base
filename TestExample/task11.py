# Вычислите значение выражения |x−5|−sinx3+x2+2014−−−−−−−−√cos2x−3 при x=−2.34.
# Ответ: -1.76911 (проверено!)

x = -2.34


import math
result = ((abs(x - 5) - math.sin(x)) / 3) + math.sqrt(x**2+2014)*math.cos(2 * x) - 3
result1 = (abs(x - 5) - math.sin(x)) / 3
second = x ** 2 + 2014
r = math.sqrt(second)


cos = math.cos(2 * x)
y = r * cos - 3
z = y + result1
print(z)
print(result)


