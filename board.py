import piece

"""
The board contains:
- The pieces
- The location of the pieces
- The board
- Possible Stat Fields
- The board only needs to contain the current position of all the pieces
    The game itself will hold the moves etc...

The board needs to be drawable
"""


class Board:
    def __init__(self):
        self.board_pieces = []
        self.board_grid = {}

    def new_board(self):
        # n = 0 could be white and n = 1 could be black
        # having i range 0,8 could define the pawns when n = 0 for white and n = 1 for black
        pass

