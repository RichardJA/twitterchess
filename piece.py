'''
this holds the individual pieces
- I need to figure out how to store how the different pieces can move.
- This becomes complicated especially when figuring out pawns / en passant / castling etc
'''


class Piece:
    def __init__(self, p_colour, p_type):
        self.piece_active = p_colour
        self.piece_type = p_type

        # Whether the piece has been taken or not
        self.piece_active = True

    def piece_legal_move(self, start_loc, end_loc):
        # This will distinguish based on piece whether the move is legal
        pass

    def take_piece(self):
        self.piece_active = False
