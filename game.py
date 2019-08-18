import pygame
from pygame import *
from board import Board

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        pygame.init()
        width, height = 640, 640
        self.screen = pygame.display.set_mode((width, height))
        # whitePieces = player1.playerName
        # blackPieces = player2.playerName

    def game_start(self):
        running = True
        fps = 60
        clock = pygame.time.Clock()
        game_board = Board(self.player1, self.player2, self.screen)
        game_board.draw_board()
        pygame.display.flip()
        while running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print("clicked " + str(x), str(y))
                    game_board.mouse_handling(x, y)
                    game_board.draw_board()
                    pygame.display.flip()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False

NEWGAME = Game("infiltration", "frog")
NEWGAME.game_start()
