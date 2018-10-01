import pygame
import init_resources

class BoardInterface():

    def __init__(self, playerOne, playerTwo, pieces_list, tiles_list, screen):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.pieces_list = pieces_list
        self.tiles_list = tiles_list
        self.screen = screen

    def draw(self):
        self.draw_tiles()
        self.draw_pieces()

    def draw_pieces(self):
        for position in self.tiles_list:
            if position.has_piece():
                pieceimage = pygame.image.load(str(position.pos_piece().pieceImage()))
                self.screen.blit(pieceimage, (position.pos_piece().drawPosition()))
    
    def draw_tiles(self):
        for tile in self.tiles_list:
            tileImage = pygame.image.load(str(tile.drawImage()))
            self.screen.blit(tileImage, (tile.tile_position()))