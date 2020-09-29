import pygame
import init_resources

class BoardInterface():

    def __init__(self, pieces_list, tiles_list):
        self.pieces_list = pieces_list
        self.tiles_list = tiles_list
        pygame.init()
        width, height = 640, 640
        self.screen = pygame.display.set_mode((width, height))

    def draw(self):
        self.draw_tiles()
        self.draw_pieces()

    def draw_tiles(self):
        for tile in self.tiles_list:
            tile_image = pygame.image.load(str(tile.draw_image()))
            self.screen.blit(tile_image, (tile.tile_position()))
    
    def draw_pieces(self):
        for tile in self.tiles_list:
            if (tile.has_piece()):
                piece = tile.pos_piece()
                piece_image = pygame.image.load(str(piece.piece_image()))
                self.screen.blit(piece_image, (piece.draw_position()))