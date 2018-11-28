"""
final.py
~Game Operation~
Rie Kurita
8 Novemeber, 2018
"""

import pygame
from pygame.locals import *
import board
import sys
import game_state
import time

empty = 0
black = 1
white = 2

class Othello:
    def __init__(self):
        self.state = game_state.GameState()
        self.board = board.Board()
        self.playing = self.state.human
        self.other = self.state.computer

    def run(self):
        self.board.game()
        self.board.show_quit()
        self.board.update(self.state.board, 2, 2)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if self.state.gameover():
                whites, blacks, empties = self.state.count_stones()
                if whites > blacks:
                    winner = white
                elif blacks > whites:
                    winner = black
                else:
                    winner = None
                break
            if self.state.get_clickable(self.playing) != []:
                self.current_board = self.state.get_move(self.playing)
                whites, blacks, empties = self.state.count_stones()
                self.board.update(self.state.board, blacks, whites)
            self.playing, self.other = self.other, self.playing

        self.board.show_winner(winner)
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    response = pygame.mouse.get_pos()
                    if response[0] >= 238 and response[0] <= 271 and response[1] >= 330 and response[1] <= 348:
                        self.restart()
                    if response[0] >= 366 and response[0] <= 398 and response[1] >= 330 and response[1] <= 348:
                        sys.exit(0)

    def restart(self):
        self.state = game_state.GameState()
        self.run()


def main():
    game = Othello()
    game.run()

if __name__ == '__main__':
    main()
