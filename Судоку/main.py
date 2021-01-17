import os
from modules import *

def start_game():
    # начало вступления
    print("Привет игрок!")
    print("В этой программе есть 2 режима решения судоку:")
    print("1) Режим игры для пользователя")
    print("2) Режим игры для компьютера")
    print("Какой из них тебе по душе?")
    print()
    print("**Чтобы выйти, необходимо написать - выход**\n")

    modes = ["1", "2", "режим игры для пользователя",
            "режим игры для компьютера", "выход"]

    game_mode = input("Выберите режим игры(можно цифру): ")

    while game_mode not in modes:
        print("Такой команды нет, попробуйте еще раз!")
        game_mode = input("Выберите режим игры(можно цифру): ")
    # конец вступления

    game = GameSess()
    board = game.load_table(grid().get_mixed_table())

    if (game_mode == "1") or (game_mode == "режим игры для пользователя"):
        print("Вы выбрали режим игры для пользователя.")
        print("Вам предстоит вводить команды в формате: Строка, Колонка, Число.")
        print("Номера колонок и строк начинаются с 1.")
        print("Пример: 2 1 9\n")
        if "saved_game.pkl" in os.listdir():
            print("У вас есть сохранение, хотите продолжить? Да/Нет")
            string = input().strip().lower()
            while string not in ["да", "нет"]:
                print("Такой команды нет, попробуйте еще раз!")
                string = input().strip().lower()

            if string == "да":
                board = load_game()
                if board == None:
                    return
            else:
                board = new_game(game, board)
                if board == None:
                    return
        else:
            board = new_game(game, board)
            if board == None:
                return

        if checker(board):
            game.print("Поздравляю, вы решили судоку!")
        else:
            game.print("К сожелению, вам не удалось решить судоку.")

    elif (game_mode == "2") or (game_mode == "режим игры для компьютера"):
        board = puzzle(board, random.randint(1, 80))
        solved = solve(read(board))
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    print_field(board)
                    board[i][j] = solved[i][j]
                    print(f"Строка: {i + 1} Колонка: {j + 1} Значение: {solved[i][j]}")

start_game()