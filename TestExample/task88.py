# Найти произведение 5⋅6⋅7⋅...⋅13.
n = 13
a = 5
result = 1

for i in range(a, n + 1, 1):
   result = result * i
   print(result)