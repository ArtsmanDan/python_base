a = 5
b = 2
c = 1
print(a + b + c)

print(a / b + c)

print((a + b + c)/3)
number = 1

while number < 15:
    print(f"число = {number + 1}")
    number += 1

for number in range(15):
    if number % 2 == 0:
        print(number)


a = {2, 3, 5}
summ = 0
for i in a:
    summ += i
mean = summ / len(a)
print(mean)


