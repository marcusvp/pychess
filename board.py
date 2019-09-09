import pygame
import init_resources

from player import Player
from board_interface import BoardInterface
from move import Move
from pygame import *

class Board():

    def __init__(self, playerOne, playerTwo):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.pieces_list = []
        self.captured_pieces_list = []
        self.position_list = []
        self.init_board()
        self.set_pieces()
        self.interface = BoardInterface(playerOne, playerTwo, self.pieces_list, self.position_list)
        self.piece_movement = Move(self.position_list, self.pieces_list, self.captured_pieces_list)
        self.turn = "white"
        

    def start_game(self):
        self.game_loop()

    def game_loop(self):
        running = True
        fps = 60
        clock = pygame.time.Clock()
        self.flip_board()
        self.draw_board()
        pygame.display.flip()
        while running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print("clicked " + str(x), str(y))
                    self.board_handling(x, y)
                    self.draw_board()
                    pygame.display.flip()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False

    def draw_board(self):
        self.interface.draw()

    def init_board(self):
        init_resources.init_pieces(self)
        init_resources.init_positions(self)

    def set_pieces(self):
        for position in self.position_list:
            for piece in self.pieces_list:
                if piece.X() == position.X() and piece.Y() == position.Y():
                    position.set_piece(piece)
    
    def remove_pieces(self):
        for position in self.position_list:
            position.remove_piece()
    
    def board_handling(self, mouse_x, mouse_y):
        if mouse_x < 640 and mouse_y < 640:
            if self.piece_movement.move_piece(mouse_x, mouse_y):
                self.change_turn()
    
    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def flip_board(self):
        self.remove_pieces()
        for position in self.position_list:
            position.flip()
        for piece in self.pieces_list:
            piece.flip()
        self.set_pieces()