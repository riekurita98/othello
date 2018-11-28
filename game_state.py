"""
game_state.py
~game_state class~
Rie Kurita
8 Novemeber, 2018
"""

empty = 0
black = 1
white = 2
infinity = 999999999
max = 0
min = 1
human = "human"
computer = "computer"

import board
from copy import deepcopy

class GameState:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        self.board[3][4] = black
        self.board[4][3] = black
        self.board[3][3] = white
        self.board[4][4] = white
        self.clickable = [[9, 9]]
        self.human = black
        self.computer = white
        self.graphics_board = board.Board()


    def get_item(self, i, j):
        return self.board[i][j]

    def check(self, i, j, color):
        if color == black:
            other = white
        else:
            other = black
        places = []
        k = 0
        l = 0

        #topleft
        if i - 1 >= 0 and j - 1 >= 0 and self.board[i - 1][j - 1] == other:
            k = i - 1 - 1
            l = j - 1 - 1
            while k >= 0 and l >= 0 and self.board[k][l] == other:
                k = k - 1
                l = l - 1
            if k >= 0 and l >= 0 and self.board[k][l] == 0:
                places = places + [(k, l)]
        #top
        if i - 1 >= 0 and self.board[i - 1][j] == other:
            k = i - 1 - 1
            while k >= 0 and self.board[k][j] == other:
                k = k - 1
            if k >= 0 and self.board[k][j] == 0:
                places = places + [(k, j)]
        #topright
        if i - 1 >= 0 and j + 1 < 8 and self.board[i - 1][j + 1] == other:
            k = i - 1 - 1
            l = j + 1 + 1
            while k >= 0 and l < 8 and self.board[k][l] == other:
                k = k - 1
                l = l + 1
            if i >= 0 and l < 8 and self.board[k][l] == 0:
                places = places + [(k, l)]
        #left
        if j - 1 >= 0 and self.board[i][j - 1] == other:
            l = j - 1 - 1
            while l >= 0 and self.board[i][l] == other:
                l = l - 1
            if l >= 0 and self.board[i][l] == 0:
                places = places + [(i, l)]
        #right
        if j + 1 < 8 and self.board[i][j + 1] == other:
            l = j + 1 + 1
            while l < 8 and self.board[i][l] == other:
                l = l + 1
            if l < 8 and self.board[i][l] == 0:
                places = places + [(i, l)]
        #bottomleft
        if i + 1 < 8 and j - 1 >= 0 and self.board[i + 1][j - 1] == other:
            k = i + 1 + 1
            l = j - 1 - 1
            while k < 8 and l >= 0 and self.board[k][l] == other:
                k = k + 1
                l = l - 1
            if k < 8 and l >= 0 and self.board[k][l] == 0:
                places = places + [(k, l)]
        #bottom
        if i + 1 < 8 and self.board[i + 1][j] == other:
            k = i + 1 + 1
            while k < 8 and self.board[k][j] == other:
                k = k + 1
            if k < 8 and self.board[k][j] == 0:
                places = places + [(k, j)]
        #bottomright
        if i + 1 < 8 and j + 1 < 8 and self.board[i + 1][j + 1] == other:
            k = i + 1 + 1
            l = j + 1 + 1
            while k < 8 and l < 8 and self.board[k][l] == other:
                k = k + 1
                l = l + 1
            if k < 8 and l < 8 and self.board[k][l] == 0:
                places = places + [(k, l)]
        return places

    def get_clickable(self, color):
        if color == black:
            other = white
        else:
            other = black
        places = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color:
                    places = places + self.check(i, j, color)
        places = list(set(places))
        self.clickable = places
        return self.clickable

    def changecolor(self, move, color):
        if move in self.get_clickable(color):
            self.board[move[0]][move[1]] = color
            for i in range(1, 9):
                self.flip(i, move, color)

    def get_move(self, color):
        if color == white:
            move = self.get_computer_move()
            self.changecolor(move, white)
        if color == black:
            valid_moves = self.get_clickable(black)
            while True:
                move = self.graphics_board.get_mouse_input()
                if move in valid_moves:
                    break
            self.changecolor(move, black)
        return self.board

    def flip(self, direction, position, color):
        #topleft
        if direction == 1:
            vertical = -1
            horizontal = - 1
        #top
        elif direction == 2:
            vertical = -1
            horizontal = 0
        #topright
        elif direction == 3:
            vertical = -1
            horizontal = 1
        #left
        elif direction == 4:
            vertical = 0
            horizontal = -1
        #right
        elif direction == 5:
            vertical = 0
            horizontal = 1
        #bottomleft
        elif direction == 6:
            vertical = 1
            horizontal = -1
        #bottom
        elif direction == 7:
            vertical = 1
            horizontal = 0
        #bottomright
        elif direction == 8:
            vertical = 1
            horizontal = 1

        i = position[0] + vertical
        j = position[1] + horizontal

        if color == white:
            other = black
        else:
            other = white
        places = []

        if i in range(8) and j in range(8) and self.board[i][j] == other:
            places = places + [(i, j)]
            i = i + vertical
            j = j + horizontal
            while i in range(8) and j in range(8) and self.board[i][j] == other:
                places = places + [(i, j)]
                i = i + vertical
                j = j + horizontal
            if i in range(8) and j in range(8) and self.board[i][j] == color:
                for p in places:
                    self.board[p[0]][p[1]] = color

    def get_computer_move(self):
        saved_board = self.board
        fintional_board = []
        move_row = None
        move_col = None
        best_move = None
        white_stone_count = 0
        move = None
        legal_moves = self.get_clickable(white)
        for row in range(8):
            for col in range(8):
                if (col, row) in legal_moves:
                    self.board = deepcopy(saved_board)
                    for i in range(1, 9):
                        self.flip(i, (col, row), white)
                    w = self.count_stones()[0]
                    if w > white_stone_count:
                        white_stone_count = w
                        best_move = (col, row)
        self.board = saved_board
        return best_move

    def count_stones(self):
        whites = 0
        blacks = 0
        empties = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == white:
                    whites += 1
                elif self.board[i][j] == black:
                    blacks += 1
                else:
                    empties += 1
        return whites, blacks, empties

    def gameover(self):
        self.whites = self.count_stones()[0]
        self.blacks = self.count_stones()[1]
        self.empties = self.count_stones()[2]
        if self.whites == 0 or self.blacks == 0 or self.empties == 0:
            return True
        elif self.clickable == []:
            return True
        else:
            return False
