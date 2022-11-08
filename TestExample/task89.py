# Найти сумму  1+4+7+11+...+112.


n = 112
a = 1
b = 3
c = 4
result = 0

while a <= 112:
    result = result + a
    print(result)
    result = result + b
    print(result)
    result = result + c
    print(result)
    a = a + 1

n = 112
i = 1
print(i)
while i <= 112:
    i = i + 3
    print(i)
    i = i + 3
    print(i)
    i = i + 3
    print(i)