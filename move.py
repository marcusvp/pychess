import pygame

class Move():

    def __init__(self, position_list, pieces_list, captured_pieces_list):
        self.position_list = position_list
        self.pieces_list = pieces_list
        self.captured_pieces_list = captured_pieces_list
        self.return_positions = []

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

    def move_piece(self, mouseX, mouseY, turn, color):
        for position in self.position_list:
            if position.has_piece():
                if position.was_clicked(mouseX, mouseY):
                    if position.pos_piece().is_selected():
                        position.unselect_piece()
                    else:
                        sel_position = self.selected_position()
                        if sel_position != None:
                            if position.pos_piece().piece_color() != sel_position.pos_piece().piece_color():
                                temp_piece = position.pos_piece()
                                self.gen_return_positions(sel_position.X(), sel_position.Y(), position.X(), position.Y())                   
                                self.captured_pieces_list.append(temp_piece)
                                #self.pieces_list.remove(temp_piece)
                                return True
                        else:
                            if position.pos_piece().piece_color() == turn and position.pos_piece().piece_color() == color:
                                self.unselect_pieces()
                                position.select_piece(self.position_list) #  select piece clicked
                                return False
            else:
                if position.was_clicked(mouseX, mouseY): # finding clicked position
                    sel_position = self.selected_position() # previously clicked piece's position
                    if sel_position:
                        self.gen_return_positions(sel_position.X(), sel_position.Y(), position.X(), position.Y())
                        return True
        return False
    
    def move_network(self, positions):
        x_start, y_start, x_end, y_end = [positions[i] for i in range(4)]
        for position in self.position_list:
            if position.X() == x_start and position.Y() == y_start:
                start_pos = position
            if position.X() == x_end and position.Y() == y_end:
                end_pos = position
        start_pos.pos_piece().gen_legal_moves(self.position_list)
        if start_pos.move_piece(end_pos):
            print("move_network:", start_pos.X(), start_pos.Y(), end_pos.X(), end_pos.Y())
            return True
        return False
    
    def gen_return_positions(self, sel_pos_x, sel_pos_y, pos_x, pos_y):
        self.return_positions.clear()
        self.return_positions.append(sel_pos_x)
        self.return_positions.append(sel_pos_y)
        self.return_positions.append(pos_x)
        self.return_positions.append(pos_y)
        
    def moving_pos_list(self):
        return self.return_positions
    