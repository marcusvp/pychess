import pygame
import flipper

class Position():
    
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.tile_image = image
        self.draw_image = image
        self.highlighted_image = "resources/board/highlighted_board.png"
        self.rectangle = pygame.Rect(x * 80, y * 80, 80, 80)
        self.has_Piece = False
        self.piece = None

    def X(self):
        return self.x
    
    def Y(self):
        return self.y

    def drawImage(self):
        return self.draw_image

    def pos_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece
        self.has_Piece = True
        self.piece.unselect()
        print("set piece at " + str(self.x), str(self.y))

    def has_piece(self):
        return self.has_Piece

    def select_piece(self, pos_list):
        self.piece.select(pos_list)
        self.highlight_square()

    def unselect_piece(self):
        self.piece.unselect()
        self.draw_image = self.tile_image

    def remove_piece(self):
        self.has_Piece = False
        self.piece = None
        #print("removed piece at " + str(self.x), str(self.y))

    def move_piece(self, end_pos):
        if self.piece.move(end_pos):
            self.remove_piece()
            self.draw_image = self.tile_image
        else:
            self.unselect_piece()

    def tile_position(self):
        return self.x * 80, self.y * 80

    def was_clicked(self, x, y):
        return self.rectangle.collidepoint(x, y)

    def highlight_square(self):
        self.draw_image = self.highlighted_image

    def flip(self):
        self.x = flipper.flip_map[self.x]
        self.y = flipper.flip_map[self.y]
        self.rectangle = pygame.Rect(self.x * 80, self.y * 80, 80, 80)

    
        

