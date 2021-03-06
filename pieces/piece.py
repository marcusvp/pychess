from legal_pos import LegalPosition
import flipper

class Piece():

    def __init__(self, x, y, color, image):
        self.x = x
        self.y = y
        self.vis_x = x
        self.vis_y = y
        self.color = color
        self.image = image
        self.legal_moves = []
        self.selected = False

    def piece_color(self):
        return self.color

    def piece_image(self):
        return self.image

    def draw_position(self):
        return self.vis_x * 80, self.vis_y * 80    

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def is_legal(self, x, y, pos_list):
        print("generic legal")
        return True
    
    def gen_legal_moves(self, pos_list):
        self.legal_moves.clear()
        for x in range(8):
            for y in range(8):
                if self.is_legal(x, y, pos_list):
                    self.legal_moves.append(LegalPosition(x, y))
        for position in self.legal_moves:
            print("position " + str(position.X()), str(position.Y()) + " is legal for " + str(self))

    def compare_legal(self, position):
        for legal_pos in self.legal_moves:
            if position.X() == legal_pos.X() and position.Y() == legal_pos.Y():
                return True        
        print("not a legal move")
        return False

    def move(self, position):
        print("piece tried moving ", self.X(), self.Y(), position.X(), position.Y())
        if self.compare_legal(position):
            self.x, self.y = position.X(), position.Y()
            self.vis_x, self.vis_y = position.vis_pos()
            #self.x = position.X()
            #self.y = position.Y()
            position.set_piece(self)
            return True
        return False

    def is_selected(self):
        return self.selected

    def select(self, pos_list):
        self.selected = True
        self.gen_legal_moves(pos_list)

    def unselect(self):
        self.selected = False

    def flip(self, position):
        #self.x, self.y = position.X(), position.Y()
        self.vis_x, self.vis_y = position.vis_pos()
        position.set_piece(self)