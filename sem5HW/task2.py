# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import itertools
import random

number_candies = 56
min_candies = 1
max_candies = 28
last_x = 0

name_game = 'Конфетный счастливчик'
descript = f'''Условие задачи: На столе лежит {number_candies} конфета. Играют два игрока делая ход друг после друга. 
            Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {max_candies} конфет. 
            Все конфеты оппонента достаются сделавшему последний ход. '''

print(name_game)
print(descript)

list_player = ['player1', 'player2']
foo = itertools.cycle((0, 1))
who_plays = next(foo)
for i in range(random.randint(1, 10)):
    who_plays = next(foo)
while number_candies > 0:
    print(f'осталось {number_candies} конфет')
    print(f'Ходит игрок {list_player[who_plays]}')
    print(f'Введите количество конфет от {min_candies} до {max_candies}')
    last_x = int(input(f'{list_player[who_plays]}, введите количество конфет которое вы возьмете: '))
    if last_x > max_candies or last_x < min_candies or last_x > number_candies:
        print('Ошибка')
        continue
    number_candies -= last_x
    if number_candies == 0:
        break
    who_plays = next(foo)
print(f'осталось {number_candies} конфет')
print(f'победитель игры {list_player[who_plays]}, Последний его ход {last_x} конфет')
