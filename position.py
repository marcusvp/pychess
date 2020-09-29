import pygame
import flipper

class Position():
    
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.vis_x = x
        self.vis_y = y
        self.tile_image = image
        self.drawn_image = image
        self.highlighted_image = "resources/board/highlighted_board.png"
        self.rectangle = pygame.Rect(x * 80, y * 80, 80, 80)
        self.has_Piece = False
        self.piece = None

    def X(self):
        return self.x
    
    def Y(self):
        return self.y
    
    def vis_pos(self):
        return self.vis_x, self.vis_y

    def draw_image(self):
        return self.drawn_image

    def pos_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.remove_piece()
        self.piece = piece
        self.has_Piece = True
        self.piece.unselect()
        #print("set piece at " + str(self.x), str(self.y))

    def has_piece(self):
        return self.has_Piece

    def select_piece(self, pos_list):
        self.piece.select(pos_list)
        self.highlight_square()

    def unselect_piece(self):
        self.piece.unselect()
        self.drawn_image = self.tile_image

    def remove_piece(self):
        self.has_Piece = False
        self.piece = None
        self.drawn_image = self.tile_image
        #print("removed piece at " + str(self.x), str(self.y))

    def move_piece(self, end_pos):
        if self.piece.move(end_pos):
            self.remove_piece()
            self.drawn_image = self.tile_image
            return True
        else:
            self.unselect_piece()
        return False

    def capture_piece(self, end_pos):
        if self.has_piece():
            if self.piece.move(end_pos):
                self.remove_piece()
                self.drawn_image = self.tile_image
                return True
            else:
                self.unselect_piece()
        return False

    def tile_position(self):
        return self.vis_x * 80, self.vis_y * 80

    def was_clicked(self, x, y):
        return self.rectangle.collidepoint(x, y)

    def highlight_square(self):
        self.drawn_image = self.highlighted_image

    def flip(self):
        self.vis_x, self.vis_y = flipper.flip_map[self.vis_pos()[0]], flipper.flip_map[self.vis_pos()[1]]
        self.rectangle = pygame.Rect(self.vis_x * 80, self.vis_y * 80, 80, 80)
        if self.has_piece():
            self.piece.flip(self)


    
        

