import pygame
import init_resources

from player import Player
from board_interface import BoardInterface
from move import Move
from pygame import *

class Board():

    def __init__(self):
        self.pieces_list = []
        self.captured_pieces_list = []
        self.position_list = []
        self.init_board()
        self.set_pieces()
        self.interface = BoardInterface(self.pieces_list, self.position_list)
        self.piece_movement = Move(self.position_list, self.pieces_list, self.captured_pieces_list)
        self.turn = "white"
        self.status_label = "connecting"
        self.players_label = "0 players"
        

    def start_game(self):
        self.game_loop()

    def game_loop(self):
        fps = 60
        clock = pygame.time.Clock()
        self.draw_board()
        pygame.display.flip()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.game_started and self.turn == self.net_color():
                x, y = event.pos
                print("clicked " + str(x), str(y))
                self.board_handling(x, y)
                self.draw_board()
                pygame.display.flip()
            elif event.type == KEYDOWN and event.key == K_TAB:
                self.flip_board()
                self.draw_board()
                pygame.display.flip()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
                    
    def commence_game(self):
        self.game_started = True

    def draw_board(self):
        self.interface.draw()

    def init_board(self):
        init_resources.init_positions(self)
        init_resources.init_pieces(self)
        
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
            if self.piece_movement.move_piece(mouse_x, mouse_y, self.turn, self.color):
                self.clients_move_piece(self.piece_movement.moving_pos_list())
    
    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
        print("changed turn to", self.turn)

    def flip_board(self):
        for position in self.position_list:
            position.flip()