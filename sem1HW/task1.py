# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def test_day(num_day):
    result = True
    if 0 < num_day < 6: result = False
    return result


num = 5
print(num, "-> ", test_day(num))