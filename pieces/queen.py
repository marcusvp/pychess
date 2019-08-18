from pieces.piece import Piece

class Queen(Piece):
    
    def is_legal(self, x, y, pos_list):
        if x == self.X():
            return self.check_y(x, y, pos_list)
        elif y == self.Y():
            return self.check_x(x, y, pos_list)
        elif x > self.X():
            return self.check_right_diags(x, y, pos_list)
        elif x < self.X():
            return self.check_left_diags(x, y, pos_list)

    def check_x(self, x, y, pos_list):
        print("checking " + str(x) + ", " + (str(y)))
        if x > self.X():
            offset = 1
        else:
            offset = -1
        for i in range(self.X(), x, offset):
            print(str(i) + " to " + str(x) + " as " + str(self.X()) + "," + str(self.Y()) + " with " + str(offset) + " as offset")
            for position in pos_list: # checking y positions from rook to destination
                if position.Y() == self.Y() and position.X() == i and position.X() != self.X():
                    print("position check " + str(i), str(position.X()))
                    if position.has_piece():
                        print(str(position.Y()), str(position.X()) + " has piece")
                        return False
        return True


    def check_y(self, x, y, pos_list):
        print("checking " + str(x) + ", " + (str(y)))
        if y > self.Y():
            offset = 1
        else:
            offset = -1
        for i in range(self.Y(), y, offset):  # x is correct, i is not
            print(str(i) + " to " + str(y) + " as " + str(self.X()) + "," + str(self.Y()) + " with " + str(offset) + " as offset")
            for position in pos_list: # checking x positions from rook to destination
                if position.X() == self.X() and position.Y() == i and position.Y() != self.Y():
                    print("position check " + str(i), str(position.Y()))
                    if position.has_piece():
                        print(str(position.X()), str(position.Y()) + " has piece")
                        return False
        return True
    
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