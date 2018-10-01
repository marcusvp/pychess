import pygame
from board import Board

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        pygame.init()
        width, height = 800, 640
        self.screen = pygame.display.set_mode((width, height))
        # whitePieces = player1.playerName
        # blackPieces = player2.playerName

    def gameStart(self):
        game_board = Board(self.player1, self.player2, self.screen)
        while 1:
            game_board.draw_board()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print("clicked " + str(x), str(y))
                    game_board.mouse_handling(x, y)
                    game_board.draw_board()     
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

NEWGAME = Game("infiltration", "frog")
NEWGAME.gameStart()
