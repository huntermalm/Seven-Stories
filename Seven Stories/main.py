"""Main module to execute the game

Running this module will execute the game loop.  This module is intended to be
a very simple starting point for the game.  If this module is running on the
interpreter as the main program, then the main() function will execute.

"""
import game


def main():
    """
    This is the only function in this module.  It first loads the game_map,
    and then calls the game.play_game() function with the loaded game_map.
    Notice how game.play_game() is being stored as arg.  It does not always
    return an arg.  This arg allows a user's action to affect higher levels of
    the game.  Only very special cases should make use of this, such as
    quitting is used here.
    """
    game_map = game.load_options()
    print("--------------------------------------------")
    arg = game.play_game(game_map)

    if arg == "quit":
        return


if __name__ == "__main__":
    main()
