import pygame
import init_resources

class BoardInterface():

    def __init__(self, playerOne, playerTwo, pieces_list, tiles_list):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
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
            tileImage = pygame.image.load(str(tile.drawImage()))
            self.screen.blit(tileImage, (tile.tile_position()))
            
    def draw_pieces(self):
        for piece in self.pieces_list:
            piece_image = pygame.image.load(str(piece.pieceImage()))
            self.screen.blit(piece_image, (piece.drawPosition()))