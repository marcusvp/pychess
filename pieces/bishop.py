from pieces.piece import Piece

class Bishop(Piece):

    def is_legal(self, x, y, pos_list):
        if x > self.X():
            return self.check_right_diags(x, y, pos_list)
        elif x < self.X():
            return self.check_left_diags(x, y, pos_list)

    def check_right_diags(self, x, y, pos_list):
        if y > self.Y():
            offset = 1
        else:
            offset = -1
        is_candidate = False
        if (abs(self.X() - x) == abs(self.Y() - y)):
            is_candidate = True
        if is_candidate:
            for position in pos_list:
                i = self.X()
                for j in range(self.Y(), y, offset):
                    if position.X() == i and position.Y() == j and position.X() != self.X():
                        if position.has_piece():
                            print(str(position.Y()), str(position.X()) + " has piece")
                            return False
                    i += 1
            return True
        return False
    
    def check_left_diags(self, x, y, pos_list):
        if y > self.Y():
            offset = 1
        else:
            offset = -1
        is_candidate = False
        if (abs(self.X() - x) == abs(self.Y() - y)):
            is_candidate = True
        if is_candidate:
            for position in pos_list:
                i = self.X()
                for j in range(self.Y(), y, offset):
                    if position.X() == i and position.Y() == j and position.X() != self.X():
                        if position.has_piece():
                            print(str(position.Y()), str(position.X()) + " has piece")
                            return False
                    i -= 1
            return True
        return False