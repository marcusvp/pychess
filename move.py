import pygame

class Move():

    def __init__(self, position_list):
        self.position_list = position_list

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
                            sel_position.move_piece(position)
                        else:
                            self.unselect_pieces()
                            position.select_piece() # select piece clicked
            else:
                if position.was_clicked(mouseX, mouseY): # finding clicked position
                    sel_position = self.selected_position() # previously clicked piece's position
                    if sel_position != None:    
                        sel_position.move_piece(position)

    