def show_field(field):
    print("  0 1 2")
    for i in range(len(field)):
        print(i, *field[i])

def user_input(field):
    while True:
        try:
            y = int(input("введите координату столбца: "))
            x = int(input("введите координату строки: "))
        except ValueError:
            print("\033[31m {}" .format(''))
            print('!!! координатой должна быть цифра')
            print("\033[0m {}" .format(''))
            continue
        if not(0 <= x < 3 and 0 <= y < 3):
            print("\033[31m {}" .format(''))
            print('!!! координата вне поля')
            print("\033[0m {}" .format(''))
            continue
        if field[x][y] != "-":
            print("\033[31m {}" .format(''))
            print('!!! поле уже занято')
            print("\033[0m {}" .format(''))
            continue
        break
    return x, y

def check_status(field):
    if field[1][1] == field[2][0] == field[0][2] != '-' or field[1][1] == field[0][0] == field[2][2] != '-':
        return True
    for i in range(3):
        for j in range(3):
            if field[i][j] != '-':
                if field[i][j] == field[i][j-1] == field[i][j-2] or field[i][j] == field[i-1][j] == field[i-2][j]:
                    return True

field_ = [['-']*3 for i in range(3)]
print('')
print("\033[35m {}" .format('--- Начинаем игру Крестики-Нолики! ---'))
print("\033[0m {}" .format(''))
show_field(field_)
user_turn = 0
while True:
    if user_turn % 2 == 0:
        user = 'X'
        user_name = 'крестик'
    else:
        user = 'O'
        user_name = 'нолик'
    print("\033[34m {}" .format(''))
    print(f'--- Ходит {user_name}! ---')
    print("\033[0m {}" .format(''))
    x, y = user_input(field_)
    field_[x][y] = user
    print('')
    show_field(field_)
    if check_status(field_) and user_turn > 3:
        print("\033[31m {}" .format(''))
        print(f'--- Выиграл {user_name}! ---')
        print("\033[0m {}" .format(''))
        break
    if user_turn == 8:
        print("\033[31m {}" .format(''))
        print('--- Ничья! ---')
        print("\033[0m {}" .format(''))
        break
    user_turn += 1
print("\033[35m {}" .format('--- Спасибо за игру! ---\n'))