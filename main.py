import random

# размеры поля
N = 10
M = 10

# количество яблок
APPLE_COUNT = random.randint(1, 7)

# символы для отображения поля
EMPTY = chr(46)  # символ '.'
WALL = chr(35)  # символ '#'
APPLE = chr(64)  # символ '@'
PLAYER = 'P'

# создаем пустое поле
FIELD = [[EMPTY for j in range(M)] for i in range(N)]

# начальная позиция игрока
PLAYER_I = random.randint(1, N - 2)
PLAYER_J = random.randint(1, M - 2)

# Начальный счет
score = 0


# Функция для генерации лабиринта
def generate_maze():
    # заполняем поле стенами
    for i in range(N):
        FIELD[i][0] = WALL
        FIELD[i][M-1] = WALL
    for j in range(M):
        FIELD[0][j] = WALL
        FIELD[N-1][j] = WALL

    # генерируем лабиринт
    for i in range(2, N-2, 2):
        for j in range(2, M-2, 2):
            FIELD[i][j] = WALL
            if random.random() < 0.5:
                FIELD[i-1][j] = WALL
            else:
                FIELD[i][j-1] = WALL


# Функция для размещения яблок на поле
def place_apples():
    count = 0
    while count < APPLE_COUNT:
        i = random.randint(0, N-1)
        j = random.randint(0, M-1)
        if FIELD[i][j] == EMPTY:
            FIELD[i][j] = APPLE
            count += 1


# Функция для отображения поля
def print_field():
    print('\n'*100)
    for i in range(N):
        for j in range(M):
            if i == PLAYER_I and j == PLAYER_J:
                print(PLAYER, end=' ')
            else:
                print(FIELD[i][j], end=' ')
        print()


# Функция для перемещения игрока
def move_player(key):
    global PLAYER_I, PLAYER_J, score
    if key == 'w':
        if PLAYER_I > 0 and FIELD[PLAYER_I-1][PLAYER_J] != WALL:
            PLAYER_I -= 1
    elif key == 's':
        if PLAYER_I < N-1 and FIELD[PLAYER_I+1][PLAYER_J] != WALL:
            PLAYER_I += 1
    elif key == 'a':
        if PLAYER_J > 0 and FIELD[PLAYER_I][PLAYER_J-1] != WALL:
            PLAYER_J -= 1
    elif key == 'd':
        if PLAYER_J < M-1 and FIELD[PLAYER_I][PLAYER_J+1] != WALL:
            PLAYER_J += 1

    # проверяем, есть ли яблоко на новой позиции игрока
    if FIELD[PLAYER_I][PLAYER_J] == APPLE:
        score += 1
        FIELD[PLAYER_I][PLAYER_J] = EMPTY


def main(player_name):
    # генерируем лабиринт и размещаем яблоки
    generate_maze()
    place_apples()

    # игровой цикл
    while True:
        # отображаем поле и счет
        print_field()
        print('Score:', score)
        print()

        # проверяем, закончилась ли игра
        if score == APPLE_COUNT:
            print(f'Вы выиграли - {player_name}!!')
            break

        # ждем ввода направления от игрока
        player_action = input('Введите (выберите) путь (двигайтесь на клавиши w/a/s/d) и нажмите "Enter": ')

        # перемещаем игрока
        move_player(player_action)


# Функция старта игры
def start_game():
    print()
    print('Приветствую вас в игре "Яблочки"\n')

    player_name = input('Пожалуйста, введите ваше имя: ')
    print()

    print(f'{player_name}, правила просты:\n'
          '1) Соберите все яблочки (генерируются в случайном количестве и месте поля)\n'
          f'2) Веселитесь - {player_name}!\n')

    print('Справочник для начинающих:\n'
          f'\tСимвол "P" - это вы, {player_name}\n'
          '\tСимвол "@" - это яблочко (которое нужно собрать)\n'
          '\tСимвол "#" - это стена\n\n'
          '\tИнформация по передвижению:\n'
          '\t\tw - шаг вверх\n'
          '\t\ta - шаг влево\n'
          '\t\ts - шаг вниз\n'
          '\t\td - шаг вправо\n')

    is_ready = input('Если готовы, просто нажмите на клавишу "Enter": ')
    main(player_name)

if __name__ == '__main__':
    start_game()