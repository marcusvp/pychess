import pygame
from pygame import *
from board import Board

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def game_start(self):        
        game_board = Board(self.player1, self.player2)
        game_board.start_game()

NEWGAME = Game("infiltration", "frog")
NEWGAME.game_start()