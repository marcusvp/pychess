from pieces.piece import Piece

class Pawn(Piece):

    def __init__(self, player, x, y, color, image):
        Piece.__init__(self, player, x, y, color, image)
        self.first_move = True
        self.was_double_step = False

    def is_legal(self, x, y):
        offset = self.get_offset()
        if self.first_move:
            double_offset = offset * 2
            if x == self.x and y == self.y - double_offset:
                print ("double move legal")
                self.first_move = False
                self.was_double_step = True
                return True
        if x == self.x and y == self.y - offset:
            print ("pawn legal")
            return True
        else:
            return False

    def get_offset(self):
        if self.color == "black":
            return 1
        else:
            return -1
