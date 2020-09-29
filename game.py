import pygame
from pygame import *
from board import Board

class Game():

    def __init__(self):
        pass

    def game_start(self):        
        game_board = Board()
        game_board.start_game()

NEWGAME = Game()
NEWGAME.game_start()