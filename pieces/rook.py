from pieces.piece import Piece

class Rook(Piece):
    
    def is_legal(self, x, y, pos_list):
        if x == self.X():
            if y > self.Y():
                offset = 1
            else:
                offset = -1
            for i in range(self.Y(), y, offset):
                print(str(i) + " to " + str(y))
                for position in pos_list: # checking y positions from rook to destination
                    if position.Y() == i and position.Y() != self.Y():
                        print("position check" + str(position.X()), str(position.Y()))
                        print(str(position.has_piece()))
                        if position.has_piece():
                            print(str(position.X()), str(position.Y()) + " has piece")
                            return False
            return True                                 