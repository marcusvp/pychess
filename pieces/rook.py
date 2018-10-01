from pieces.piece import Piece

class Rook(Piece):
    
    def is_legal(self, x, y):
        if x == self.X() or y == self.Y():
            return True
        return False