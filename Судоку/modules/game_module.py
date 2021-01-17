import pickle
import random

class GameSess():
    def __init__(self):
        self.console = ""

    def print_field(self, field):
        for i in range(9):
            for j in range(9):
                cell = field[i][j]
                if cell == 0 or isinstance(cell, set):
                    self.print('.', end="")
                else:
                    self.print(cell, end="")
                if (j + 1) % 3 == 0 and j < 8:
                    self.print(' |', end="")
                if j != 8:
                    self.print(' ', end="")
            self.print('')
            if (i + 1) % 3 == 0 and i < 8:
                self.print("- - - + - - - + - - -\n", end="")

    def print(self, string="", end="\n"):
        self.console += str(string) + end
        print(string, end=end)

    def input(self, string):
        value = input(string).lower().strip()
        if value != "выход":
            self.console += string
            self.console += value + "\n"
        return value

    def load_table(self, table):
        self.table = table
        return table

    def save(self):
        with open("saved_game.pkl", 'wb') as f:
            pickle.dump(self, f)

    def load(self):
        with open("saved_game.pkl", 'rb') as f:
            self = pickle.load(f)
        return self

def new_game(game, board):
    n = game.input("Сколько клеточек будет заполнено? ")
    board = puzzle(board, int(n))
    empties = str(board).count("0")
    game.print("И так, вот ваша задача:\n")
    game.print_field(board)
    game.print()
    for _ in range(empties):
        string = game.input("Введите команду: ")
        game.print()
        if string == "выход":
            game.save()
            return
        row, col, val = map(int, string.split())
        board[row - 1][col - 1] = val
        game.print_field(board)
        game.print()
    return board

def load_game():
    game = GameSess().load()
    print(game.console)
    board = game.table
    empties = str(board).count("0")
    for _ in range(empties):
        string = game.input("Введите команду: ")
        game.print()
        if string == "выход":
            game.save()
            return
        row, col, val = map(int, string.split())
        board[row - 1][col - 1] = val
        game.print_field(board)
        game.print()
    return board

def puzzle(board, n):
    side = 9
    squares = side * side
    empties = squares - n
    for i in random.sample(range(squares), empties):
        board[i // side][i % side] = 0
    return board