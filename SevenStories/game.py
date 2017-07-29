"""Provide basic game functionality

The functions in this module provide the foundation for the game to operate
as it does.  These functions are considered the game's core, and therefore
live within the game.py module.

"""
import os
import pickle
from SevenStories import gamemap


def play_game(game_map, input=input):
    """Enters the main game loop

    The game loop is considered occuring while a command is in progress.  This
    is because every time the game loops, the user needs to enter a new
    command.

    The user's command is handled inside the parse.parse_command() function,
    which takes the user's input as an argument.  This function returns the
    load, which is a list of tuples.  Each tuple is created per action that
    appears inside the user's command, and each tuple stores two things
    regarding that action: a function that pertains to that particular action,
    and the action object (see wordtypes.py).

    The load obtained by the parse.parse_command() function is then passed
    to the execute() function.  This function contains code specifically
    designed to iterate over the load, unpack the tuples, and perform
    per-action operations.

    In the event that a user types an action designed to interact with higher
    levels of the game (i.e. quitting), that action function will return an
    arbitrary string.  This string is then return by the execute() function and
    stored as "arg".  The execute() function does not have to return anything.
    This arg can be continually passed up all the way to the main() function
    to let the user perform higher level actions, such as quitting the game.

    Once the execute() function completes, and there is no argument returned,
    the loop starts over again and asks the user to enter another command.

    :param game_map: The currently loaded GameMap object
    :type game_map: class GameMap
    :return: may return arg to be used at higher level
    :rtype: str or None

    """
    from SevenStories import parse

    cmd_in_prog = True
    while cmd_in_prog:
        load = parse.parse_command(input("Enter a command: "))
        arg = execute(game_map, load)

        if arg == "quit":
            return arg


def execute(game_map, load):
    """Execute all of the actions parsed from the user's command

    This function iterates over the load list, unpacking each function and
    action object, and then calls the function passing it the game_map and
    the action object.  Using this method means that every action function
    (in actions.py) must take these two parameters.  By sending the game_map,
    you're giving the action function access to everything the game_map
    contains.  The purpose of passing along the action object is because it
    will be designed to store action specific details, such as direct objects
    or even objects of prepositions.

    This is also where an arg can be passed up.  If an action function returns
    a string, it will be declared as "arg".  A set of "if-else" statements
    appears directly below this declaration, and also after every parent
    function called all the way back to the main() function.  For now, this is
    only being used to properly quit the game, however, it may be used if
    user actions ever need to affect higher levels of the game.

    If the user's action is "save", then the game_map.just_saved value will
    be set to True, otherwise False.  This check occurs per action.  This
    allows the "quit" action function to check if the user just saved, and if
    not, it will ask the user if they would like to save before quitting.

    If the user's command does not contain any actions, load will be empty.
    If the load does not contain anything, "Invalid command!" is returned
    back to the user.

    :param game_map: GameMap object to execute on
    :type game_map: class GameMap
    :param load: List of tuples formatted as (function, action_object)
    :type load: list
    :return: may return arg to be used at higher level
    :rtype: str or None

    """
    print("--------------------------------------------")
    for count, (function, action_object) in enumerate(load):
        arg = function(game_map, action_object)

        if arg == "quit":
            return arg

        if action_object.word == "save":
            game_map.just_saved = True
        else:
            game_map.just_saved = False

    if not load:
        print("Invalid command!")
    print("--------------------------------------------")


def get_saves_dir():
    """Return the saves directory

    Checks the os.name to handle differences between how operating systems
    handle slashes in directory paths.

    Also checks if the program is running from root.  Until a proper
    cross-platform system is implemented, the user may run the program in
    QPython3.  The "SevenStories" directory must be placed inside
    "/storage/emulated/0/qpython/scripts3/".  If you decide to place it
    somewhere else, you must change the os.chdir() function call below.

    :return: Saves directory
    :rtype: str

    """
    if os.name == "posix":
        if os.getcwd() == "/":  # Handles QPython3 is game directory is in scripts3
            saves_dir = "/storage/emulated/0/qpython/scripts3/SevenStories/SevenStories/saves"
        else:
            saves_dir = "{}/.SevenStories/saves/".format(os.getenv("HOME"))

    else:
        saves_dir = "{}\\SevenStories\\saves\\".format(os.getenv("LOCALAPPDATA"))

    if not os.path.exists(saves_dir):
        os.makedirs(saves_dir)

    return saves_dir


def get_simple_answer(question, input=input):
    """Return True or False based on a yes/no response to a question

    Contains a dictionary that maps the yes/no strings to True/False values.
    If the user's response appears in the dictionary, it is used as the key
    to retrieve the True/False value, which is then returned.  If the user's
    response does not appear in the dictionary, it tells the user that they
    must choose yes or no, and then loops back to obtain a repsonse again.

    :param str question: Question that can be answered with yes or no.
    :return: True or False depending on yes/no response
    :rtype: boolean

    """
    simple_answers_dict = {
        "yes": True, 'y': True, "yeah": True, "yea": True,
        "no": False, 'n': False, "nope": False
        }
    while True:
        input_answer = input(question)
        if input_answer in simple_answers_dict:
            return simple_answers_dict[input_answer]
        else:
            print("          ----------------------")
            print("Must choose yes or no.")
            print("          ----------------------")


def save_game(game_map, echo=True):
    """Saves the game_map to a file in the saves directory

    This game makes use of the pickle module for object serialization.  The
    game_map is dumped to a file as "<lowercase player name>.dat".  If it
    already exists, it will be overwritten; if not, it will be created.

    Echos by default.

    :param game_map: GameMap object to save
    :type game_map: class GameMap
    :param echo=True: Echos to console if True
    :type echo=True: boolean

    """
    with open(get_saves_dir() + game_map.player.name.lower() + ".dat", "wb") as f:
        pickle.dump(game_map, f, protocol=3)

    if echo:
        print("Saved {}.".format(game_map.player.name))


def load_game(character_name, echo=True):
    """Loads and returns a game_map from a file in the saves directory

    This function returns a game_map object from a file formatted
    "<character name>.dat".  The file is loaded via the pickle module.

    Echos by default.

    :param str character_name: Name of the character to load
    :param echo=True: Echos to console if True
    :type echo=True: boolean
    :return: Loaded game_map
    :rtype: class GameMap

    """
    with open(get_saves_dir() + character_name.lower() + ".dat", "rb") as f:
        game_map = pickle.load(f)

        if echo:
            print("Loaded {}.".format(character_name))

        return game_map


def reset_character(character_name, echo=True):
    """Resets a character to a fresh game_map

    First deletes the character.  Then creates a new game_map with the same
    character name.  Finally, the game_map is saved.

    Echos by default.

    :param str character_name: Name of character to reset
    :param echo=True: Echos to console if True
    :type echo=True: boolean

    """
    delete_character(character_name, echo=False)

    game_map = gamemap.GameMap(character_name)
    save_game(game_map, echo=False)

    if echo:
        print("Reset {}.".format(character_name))


def create_character(input=input):
    """Creates and returns new game_map after asking for a name

    Asks the user to enter a name.  If the name does not already exist, a new
    game_map will be created using the name and returned.  Loops until a
    non-existing name is entered.

    :return: New GameMap object based on name
    :rtype: class GameMap

    """
    while True:
        name_exists = False
        name = input("Enter a name: ")

        for file in os.listdir(get_saves_dir()):
            if name.lower() == file[:-4]:
                name_exists = True
                print("\nA character named {} already exists!\n".format(name))

        if not name_exists:
            game_map = gamemap.GameMap(name)
            save_game(game_map, echo=False)
            return game_map


def delete_character(character_name, echo=True):
    """Delete a character

    os.remove() function on a file formatted "<character name>.dat".

    Echos by default.

    :param str character_name: Name of character to delete
    :param echo=True: Echos to console if True
    :type echo=True: boolean

    """
    os.remove(get_saves_dir() + character_name.lower() + ".dat")

    if echo:
        print("Deleted {}.".format(character_name))


def load_options():
    """Provides an interface for loading, resetting, or deleting characters

    Gets a dictionary of characters based on the saves in the saves directory,
    displays them to the user, and displays a set of commands that can be
    entered by the user.  Loops until the user enters a valid command.

    The only argument the user will need to enter is the character number
    displayed alongside the character name of the charcter they would like to
    perform the command on.  This number is stored as a key in the
    character_names dictionary

    If the command requires an argument, and one is not entered, an IndexError
    exception is raised and caught.  A message is printed to the console
    formatted as "<command> what?", implying that is does not know which
    character to perform the command on.

    Function only ends once it returns a game_map.  This happens two ways.
    If the user enters "load <displayed character number>", then it will load
    and return the game_map from that character file.  Also, if there if no
    save in the saves directory, then create_character() is returned, which
    itself returns a game_map.

    :return: GameMap object if loaded or no character exists
    :rtype: class GameMap

    """
    while True:
        save_exists = False
        character_names = {}

        for count, file in enumerate(os.listdir(get_saves_dir())):
            save_exists = True
            with open(get_saves_dir() + file, "rb") as f:
                game_map = pickle.load(f)
                character_names[str(count + 1)] = game_map.player.name

        print("--------------------------------------------")

        if not save_exists:
            return create_character()

        print("Your characters:")

        for count, key in enumerate(character_names):
            print(">> {}: {}".format(key, character_names[key]))

        print("--------------------------------------------")
        print("Available options:")
        print("> new")
        print("> load [number]")
        print("> reset [number]")
        print("> delete [number]")

        while True:
            print("--------------------------------------------")
            command = input(">>> ").lower()
            print("--------------------------------------------")
            parts = command.split()

            if parts:
                if parts[0] == "new":
                    return create_character()
                else:
                    try:
                        if parts[0] == "load":
                            return load_game(character_names[parts[1]])
                        elif parts[0] == "reset":
                            reset_character(character_names[parts[1]])
                        elif parts[0] == "delete":
                            delete_character(character_names[parts[1]])
                            break
                        else:
                            print("Invalid command!")
                    except IndexError:
                        print("{} what?".format(parts[0].capitalize()))
                    except KeyError:
                        if parts[1].isdigit():
                            print("There is no character labeled '{}'.".format(parts[1]))
                        else:
                            print("You must enter the character number.")
            else:
                print("Invalid command!")
