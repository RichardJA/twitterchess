# Will need to import the board as the game contains a board
import board

"""
The game contains:
- The two usernames involved
- Whether the game is complete
- Whose turn it is next
- What player is white
- The board
- The latest image of the board
- A list of moves
    - This could be a list of lists eg [['E4'. '
- Possible Stat Fields

Each game is stored in a SQL Database
"""


class Game:
    def __init__(self, p1, p2):
        player_one = str(p1)
        player_two = str(p2)
        game_board = board.Board
        game_moves = []
