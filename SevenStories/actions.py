"""Stores action functions that affect the game map

This modules contains all of the action functions.  An action function is the
function associated with an action in the user's command.  This system uses
a dictionary, aquired by the get_action_dictionary() function in this module,
to map the string of any particular action to its corresponding function,
without calling it.  This allows all of the action functions to be stored
before they are all executed.

The function, however, is not just stored directly in the list because the
action object also needs to be stored alongside the function (as it will
contain information like direct objects and objects of prepositions).  Because
of this, the function and action object are first stored inside a tuple, and
then the tuple is stored inside the list.  This particular list is referred to
as the load.

Every action function in this module takes the same arguments: the game map,
and the action object.  This allows iterating over the load, unpacking the
tuples as "function, action_object", and calling them as
"function(game_map, action_object)".

"""


def name(game_map, action_object):
    """Display the player's name"""
    print("Name: {}".format(game_map.player.name))


def health(game_map, action_object):
    """Display the player's health"""
    print("Health: {}%".format(game_map.player.health))


def save(game_map, action_object):
    """Save the game"""
    from game import save_game
    save_game(game_map)


def quit(game_map, action_object):
    """Quit the game

    If the previous action was not "save", then this function will ask the
    player if they would like to save before quitting.  This is handled with
    an attribute called "just_saved" in the class GameMap that is set every
    time an action function is called.  Only if the action function is "save"
    will the attribute be set to True.

    To quit, this function returns a string "quit" to be a recognized argument
    all the way back to the main.main() function, which is finally returned to
    properly quit the game.

    :return: "quit" intended to be a recognized argument at higher levels
    :rtype: str

    """
    if not game_map.just_saved:
        from game import get_simple_answer
        question = "Would you like to save before quitting (y\\n)? "
        do_save = get_simple_answer(question)
        print("--------------------------------------------")
        if do_save:
            save(game_map, action_object)
            print("--------------------------------------------")

    print("Quitting..")

    return "quit"


def get_action_dictionary():
    """Returns action dictionary with action string mapped to action function

    :return: Action dictionary (action string: action function)
    :rtype: dict

    """
    action_dictionary = {
        "name": name, "health": health, "save": save, "quit": quit
        }

    return action_dictionary
