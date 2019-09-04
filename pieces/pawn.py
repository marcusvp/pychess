from pieces.piece import Piece
import flipper

class Pawn(Piece):

    def __init__(self, player, x, y, color, image):
        Piece.__init__(self, player, x, y, color, image)
        self.first_move = True
        self.was_double_step = False
        self.offset = self.get_offset()

    def is_legal(self, x, y, pos_list):
        if self.first_move:
            double_offset = self.offset * 2
            if x == self.x and y == self.y - double_offset:
                print ("double move legal")
                return True
        if x == self.x and y == self.y - self.offset:
            print ("pawn legal")
            return True
        else:
            return False

    def get_offset(self):
        if self.color == "black":
            return 1
        else:
            return -1

    def compare_legal(self, position):
        for legal_pos in self.legal_moves:
            if position.X() == legal_pos.X() and position.Y() == legal_pos.Y():
                self.first_move = False
                if self.was_double_step == True:
                    self.was_double_step = False
                if self.y == legal_pos.Y() - 2 or self.y == legal_pos.Y() + 2:
                    self.was_double_step = True
                return True        
        print("not a legal pawn move")
        return False
    
    def flip(self):
        self.x = flipper.flip_map[self.x]
        self.y = flipper.flip_map[self.y]
        self.offset *= - 1
