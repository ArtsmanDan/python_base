# Найти сумму 10+11+12+13+...+88. Материал сайта www.itmathrepetitor.ru Ответ: 3871

n = int(input(" Введите число ДО которого идет  подсчет:  "))#До каого числа производим счет?

a = int(input(" Введите число С которого начнем подсчет:  "))  # С какого числа начинаем складывать?
b = 0
c = 0
i = 0


n = n - a
while i <= n:
    b = a + i
    print(c, "+", b, end=" = ")
    c = c + b
    i = i + 1
    print(c)
sum = 0
for i in range(10, 88 + 1):
    sum += i
print(sum)

sum = 0
i = 10
while i <= 88:
    temp = sum
    sum += i
    i += 1
    print(temp, "+", i, " = ", sum)
