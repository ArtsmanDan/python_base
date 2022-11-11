# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
#
#
# test_data = [
# [["привет абв как абвышные дела?", "абв"], "привет как дела?"]
# ]
# for args, exp in test_data:
# assert remove_substr(*args) == exp
# #assert remove_substr_func(*args) == exp

test_data = "привет абв как абвышные дела?, абв, привет как дела?"


def delete_world(text):
    s = ' '
    text = list(filter(lambda l: 'абв' not in l, text.split()))
    return s.join(text)


# print(test_data.split())
text_out = delete_world(test_data)
print(text_out)
