from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.pawn import Pawn
from position import Position

def init_pieces(self):
    init_rooks(self)
    init_knights(self)
    init_bishops(self)
    init_queens(self)
    init_kings(self)
    init_pawns(self)

def init_positions(self):
    white_tile = "resources/board/white_board.png"
    black_tile = "resources/board/grey_board.png"
    for i in range (8):
        for j in range (8):
            if (i + j) % 2 == 0:
                self.position_list.append(Position(i, j, white_tile))
            else:
                self.position_list.append(Position(i, j, black_tile))

def init_rooks(self):
    white_rook = "resources/pieces/WhiteRook.png"
    black_rook = "resources/pieces/BlackRook.png"
    self.pieces_list.append(Rook(0, 0, "white", white_rook))
    self.pieces_list.append(Rook(7, 0, "white", white_rook))
    self.pieces_list.append(Rook(0, 7, "black", black_rook))
    self.pieces_list.append(Rook(7, 7, "black", black_rook))

def init_knights(self):
    white_knight = "resources/pieces/WhiteKnight.png"
    black_knight = "resources/pieces/BlackKnight.png"
    self.pieces_list.append(Knight(1, 0, "white", white_knight))
    self.pieces_list.append(Knight(6, 0, "white", white_knight))
    self.pieces_list.append(Knight(1, 7, "black", black_knight))
    self.pieces_list.append(Knight(6, 7, "black", black_knight))

def init_bishops(self):
    white_bishop = "resources/pieces/WhiteBishop.png"
    black_bishop = "resources/pieces/BlackBishop.png"
    self.pieces_list.append(Bishop(2, 0, "white", white_bishop))
    self.pieces_list.append(Bishop(5, 0, "white", white_bishop))
    self.pieces_list.append(Bishop(2, 7, "black", black_bishop))
    self.pieces_list.append(Bishop(5, 7, "black", black_bishop))

def init_queens(self):
    white_queen = "resources/pieces/WhiteQueen.png"
    black_queen = "resources/pieces/BlackQueen.png"
    self.pieces_list.append(Queen(3, 0, "white", white_queen))
    self.pieces_list.append(Queen(3, 7, "black", black_queen))

def init_kings(self):
    white_king = "resources/pieces/WhiteKing.png"
    black_king = "resources/pieces/BlackKing.png"
    self.pieces_list.append(King(4, 0, "white", white_king))
    self.pieces_list.append(King(4, 7, "black", black_king))

def init_pawns(self):
    white_pawn = "resources/pieces/WhitePawn.png"
    black_pawn = "resources/pieces/BlackPawn.png"
    for i in range(8):
        self.pieces_list.append(Pawn(i, 1, "white", white_pawn))
    for j in range(8):
        self.pieces_list.append(Pawn(j, 6, "black", black_pawn))