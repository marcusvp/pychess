import pygame

class Move():

    def __init__(self, position_list, pieces_list, captured_pieces_list):
        self.position_list = position_list
        self.pieces_list = pieces_list
        self.captured_pieces_list = captured_pieces_list

    # returns already selected position
    def selected_position(self):
        for position in self.position_list:
            if position.has_piece():                      
                if position.pos_piece().is_selected():
                    return position

    # unselect all pieces
    def unselect_pieces(self):
        for pos_selected in self.position_list:
            if pos_selected.has_piece(): 
                pos_selected.unselect_piece() 

    def move_piece(self, mouseX, mouseY):
        for position in self.position_list:
            if position.has_piece():
                if position.was_clicked(mouseX, mouseY):
                    if position.pos_piece().is_selected():
                        position.unselect_piece()
                    else:
                        sel_position = self.selected_position()
                        if sel_position != None and position.pos_piece().pieceColor() != sel_position.pos_piece().pieceColor():
                            temp_piece = position.pos_piece()
                            if sel_position.capture_piece(position):
                                self.pieces_list.remove(temp_piece)
                                self.captured_pieces_list.append(temp_piece)
                                return True
                        else:
                            self.unselect_pieces()
                            position.select_piece(self.position_list) # select piece clicked
            else:
                if position.was_clicked(mouseX, mouseY): # finding clicked position
                    sel_position = self.selected_position() # previously clicked piece's position
                    if sel_position != None: 
                        if sel_position.move_piece(position):
                            return True
        return False

    