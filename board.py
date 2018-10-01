import pygame
import init_resources
from player import Player
from board_interface import BoardInterface
from move import Move

class Board():

    def __init__(self, playerOne, playerTwo, screen):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.pieces_list = []
        self.captured_pieces_list = []
        self.position_list = []
        self.init_board()
        self.set_pieces()
        self.interface = BoardInterface(playerOne, playerTwo, self.pieces_list, self.position_list, screen)
        self.piece_movement = Move(self.position_list)

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
    
    def mouse_handling(self, mouseX, mouseY):
        if mouseX < 640 and mouseY < 640:
            self.piece_movement.move_piece(mouseX, mouseY)

            
        
                        