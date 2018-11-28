"""
board.py
~Board Class~
Rie Kurita
8 Novemeber, 2018
"""

import pygame
import sys
from pygame.locals import *
import time
import graphics

pygame.init()

empty = 0
black = 1
white = 2

class Board:
    def __init__(self):
        # window
        self.screen_size = (640, 480)
        self.board_pos = (100, 20)
        self.board = (120, 40)
        self.board_size = 400
        self.square_size = 50
        self.screen = pygame.display.set_mode(self.screen_size)

        # colors
        self.black = (0, 0, 0)
        self.back_color = (230, 230, 230)
        self.white = (255, 255, 255)
        self.white_stone = pygame.image.load("white.jpg").convert()
        self.black_stone = pygame.image.load("black.jpg").convert()
        self.board_image = pygame.image.load("board.jpg").convert()
        self.empty_tile = pygame.image.load("empty.jpg").convert()

        self.font = pygame.font.SysFont("Times New Roman", 22)


    def game(self):
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(self.back_color)
        self.screen.blit(self.background, (0, 0), self.background.get_rect())
        self.screen.blit(self.board_image, self.board_pos, self.board_image.get_rect())
        self.put_stone((3, 3), white)
        self.put_stone((4, 4), white)
        self.put_stone((3, 4), black)
        self.put_stone((4, 3), black)
        pygame.display.flip()

    def put_stone(self, position, color):
        if position == None:
            return
        position = (position[1], position[0])

        if color == black:
            tile = self.black_stone
        elif color == white:
            tile = self.white_stone
        else:
            tile = self.tip

        x = position[0] * self.square_size + self.board[0]
        y = position[1] * self.square_size + self.board[1]

        self.screen.blit(tile, (x, y), tile.get_rect())
        pygame.display.flip()

    def clear_square(self, position):
        position = (position[1], position[0])

        x = position[0] * self.square_size + self.board[0]
        y = position[1] * self.square_size + self.board[1]
        self.screen.blit(self.empty_tile, (x, y), self.empty_tile.get_rect())
        pygame.display.flip()

    def get_mouse_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()

                    if mouse_x >= 570 and mouse_x <= 590 and mouse_y >= 440 and mouse_y <= 450:
                        sys.exit(0)

                    elif mouse_x > self.board_size + self.board[0] or \
                       mouse_x < self.board[0] or \
                       mouse_y > self.board_size + self.board[1] or \
                       mouse_y < self.board[1]:
                        continue

                    position = ((mouse_x - self.board[0]) // self.square_size), \
                               ((mouse_y - self.board[1]) // self.square_size)
                    position = (position[1], position[0])
                    return position


    def update(self, board, blacks, whites):
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    self.put_stone((i, j), board[i][j])
        pygame.display.flip()

    def show_quit(self):
        quit_text = self.font.render("Quit", True, self.black)
        quit_pos = quit_text.get_rect(centerx=580, centery=450)
        self.screen.blit(quit_text, quit_pos)

    def show_winner(self, winner):
        self.screen.fill((245, 245, 245))
        font = pygame.font.SysFont("Times New Roman", 40)
        if winner == black:
            msg = font.render("You won!!", True, (230, 100, 100))
        elif winner == white:
            msg = font.render("You lost...", True, (100, 100, 230))
        else:
            msg = font.render("Tie!", True, (100, 230, 100))
        self.screen.blit(
            msg, msg.get_rect(centerx=self.screen.get_width() / 2, centery=200))
        restart_text = self.font.render("Do you want to play again?", True, self.black)
        restart_pos = restart_text.get_rect(centerx=self.screen.get_width() / 2, centery=290)
        self.screen.blit(restart_text, restart_pos)
        yes_text = self.font.render("Yes", True, self.black)
        yes_pos = yes_text.get_rect(centerx=2 * self.screen.get_width() / 5, centery=340)
        no_text = self.font.render("No", True, self.black)
        no_pos = no_text.get_rect(centerx=3 * self.screen.get_width() / 5, centery=340)
        self.screen.blit(yes_text, yes_pos)
        self.screen.blit(no_text, no_pos)
        pygame.display.flip()
