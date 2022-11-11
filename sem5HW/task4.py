# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def encode(data):
    encode_text = ''
    prev_symbol = ''
    count = 1

    if not data:
        return ''

    for symbol in data:
        if symbol != prev_symbol:
            if prev_symbol:
                encode_text += str(count) + prev_symbol
            count = 1
            prev_symbol = symbol
        else:
            count += 1
    encode_text += str(count) + prev_symbol
    return encode_text


def decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


data1 = 'В целом, конечно, высококачественный прототип будущего проекта представляет собой интересный эксперимент ' \
       'проверки вывода текущих активов. Приятно, граждане, наблюдать, как реплицированные с зарубежных источников,' \
       ' современные исследования разоблачены! С другой стороны, синтетическое тестирование требует анализа стандартных' \
       ' подходов. В рамках спецификации современных стандартов, стремящиеся вытеснить традиционное производство,' \
       ' нанотехнологии освещают чрезвычайно интересные особенности картины в целом, однако конкретные выводы,' \
       ' разумеется, разоблачены. Но разбавленное изрядной долей эмпатии, рациональное мышление однозначно определяет' \
       ' каждого участника как способного принимать собственные решения касаемо соответствующих условий активизации.' \
       ' Предварительные выводы неутешительны: высокотехнологичная концепция общественного уклада способствует' \
       ' повышению качества существующих финансовых и административных условий. Банальные, но неопровержимые выводы,' \
       ' а также представители современных социальных резервов формируют глобальную экономическую сеть' \
       ' и при этом — рассмотрены исключительно в разрезе маркетинговых и финансовых предпосылок.'
data2 = 'ddddddddsffffffffffffffffeeeeeeeeeeeeeeeeeeeeeggggggggggggbbbbbbbbbbbbvvvvvvvvvvvvvvvvrrrrrrrrrgfggggggggggggggth'
with open('sun.bmp') as file_data:
    data3 = file_data.read()
    file_data.close()

data = data3
# print(data)
encode_data = encode(data)
# print(encode_data)
print(len(data), '- размер несжатых данных')
print(len(encode_data), '- размер сжатых данных')
print(round(len(encode_data)/len(data)*100), "- процент сжатия от первоначального файла, чем меньше, тем лучше сжатие")
with open('task4encode.rle', 'w') as file_data:
    file_data.write(encode_data)
    file_data.close()
with open('task4encode.rle') as file_data:
    data_encode = file_data.read()
    file_data.close()
decode_data = decode(data_encode)
# print(decode_data)
with open('task4decode.bmp', 'w') as file_data:
    file_data.write(decode_data)
    file_data.close()
