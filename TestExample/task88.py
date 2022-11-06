# Найти произведение 5⋅6⋅7⋅...⋅13.
n = 13
a = 5
i = 0
b = 0
c = 0
while i <= n:
   b = a + i
   c = a * b
   z = c
   w = z * b

   i = i + 1
   print(z)

    #print(c, "+", b, end=" = ")