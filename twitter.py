import board
import tweepy

def connect_to_twitter():
    """
    This will create the connection to twitter
    """
    pass


def receive_command():
    """
    This gets the commands from the user and activates the corresponding action
    """
    pass


def validate_command(command):
    """
    This check the command from the user and validates it to see whether it is a valid command
    """
    command_list = ["new", "reject", "move", "board", "retire", "games", "stats", "commands", "accept"]
    if command in command_list:
        # TODO: What do I do if they pass

        pass
    else:
        # TODO: Return a fail command
        return


def validate_user(user):
    """
    Checks that the user mentioned in the tweet exists
    """
    pass


def incorrect_input_response(issue, user="", game_board=""):
    """
    Responds to the user informing them that the input / request is incorrect
    """
    # This is the dictionary of auto replies depending on the issue brought up
    # TODO: Some of these would be helpful to have the board included in the error message
    response_dict = {"no_command": "That command does not exist, you can see the command here: ",
                     "no_user": "There is no one on twitter by the name " + user,
                     "no_game": "You don't currently have an active game against " + user,
                     "no_stats": "You don't have any stats as you haven't played any games played yet",
                     "no_move": "It's not currently your move in the game againt " + user,
                     "bad_move": "Thats not a legal move in the game against " + user,
                     "game_exists": "You already have an active game against " + user,
                     "no_request": "You haven't received a request to play against " + user}

    pass
