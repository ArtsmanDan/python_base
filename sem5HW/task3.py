# Создайте программу для игры в ""Крестики-нолики"".

field = list(range(1, 10))


def draw_field(field):
    print("-" * 13)
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-" * 13)


def win_check(field):
    win_position = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_position:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def move(player_token):
    while True:
        try:
            num_field = int(input("Введите номер клетки: " + player_token + "? "))
        except:
            print("Ошибка ввода, введите корректный номер клетки")
            continue
        if 9 >= num_field >= 1:
            if str(field[num_field - 1]) not in ['X', '0']:
                field[num_field - 1] = player_token
                break
            else:
                print("Клетка занята, выберите другую")
        else:
            print("Ошибка ввода. Введите число от 1 до 9.")


def play_game(field):
    count = 0
    win = False
    while not win:
        draw_field(field)
        if count % 2 == 0:
            move('X')
        else:
            move('0')
        count += 1
        if count > 4:
            win_status = win_check(field)
            if win_status:
                draw_field(field)
                print(f'{win_status} выиграл за {count} ходов')
                break
            if count == 9:
                draw_field(field)
                print('ничья')
                break


play_game(field)
