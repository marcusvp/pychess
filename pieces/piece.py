from legal_pos import LegalPosition

class Piece():

    def __init__(self, player, x, y, color, image):
        self.player = player
        self.x = x
        self.y = y
        self.color = color
        self.image = image
        self.legal_moves = []
        self.selected = False

    def pieceColor(self):
        return self.color

    def pieceImage(self):
        return self.image

    def drawPosition(self):
        return self.x * 80, self.y * 80    

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def is_legal(self, x, y):
        return True
    
    def gen_legal_moves(self):
        self.legal_moves.clear()
        for x in range(8):
            for y in range(8):
                if self.is_legal(x, y):
                    self.legal_moves.append(LegalPosition(x, y))

    def compare_legal(self, position):
        for legal_pos in self.legal_moves:
            if position.X() == legal_pos.X() and position.Y() == legal_pos.Y():
                return True        
        print("not a legal move")
        return False

    def move(self, position):
        if self.compare_legal(position):
            self.x = position.X()
            self.y = position.Y()
            position.set_piece(self)
            return True
        return False

    def is_selected(self):
        return self.selected

    def select(self):
        self.selected = True
        self.gen_legal_moves()

    def unselect(self):
        self.selected = False