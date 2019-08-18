from pieces.piece import Piece

class Knight(Piece):
    
    def is_legal(self, x, y, pos_list):
        x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        possible_dest_x = []
        possible_dest_y = []

        for i in range(0, 8):
            x_dest = self.X() + x_moves[i]
            y_dest = self.Y() + y_moves[i]
            if (x_dest >= 0 and y_dest >= 0 and x_dest < 8 and y_dest < 8):
                possible_dest_x.append(x_dest)
                possible_dest_y.append(y_dest)
        
        for i in range (0, len(possible_dest_x)):
            if x == possible_dest_x[i] and y == possible_dest_y[i]:
                return True
        return False

