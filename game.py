import os
import pickle
import gamemap


def play_game(game_map):
    import parse

    cmd_in_prog = True
    while cmd_in_prog:
        load = parse.parse_command(input("Enter a command: "))
        arg = execute(game_map, load)

        if arg == "quit":
            return arg


def execute(game_map, load):
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
    if os.name == "posix":
        if os.getcwd() == "/":
            os.chdir("/storage/emulated/0/qpython/scripts3/Game")
        saves_dir = os.getcwd() + "/saves/"

    else:
        saves_dir = os.getcwd() + "\\saves\\"

    if not os.path.exists(saves_dir):
        os.makedirs(saves_dir)

    return saves_dir


def save_game(game_map, echo=True):
    with open(get_saves_dir() + game_map.player.name.lower() + ".dat", "wb") as f:
        pickle.dump(game_map, f, protocol=3)

    if echo:
        print("Saved {}.".format(game_map.player.name))


def load_game(character_name, echo=True):
    with open(get_saves_dir() + character_name + ".dat", "rb") as f:
        game_map = pickle.load(f)

        if echo:
            print("Loaded {}.".format(game_map.player.name))

        return game_map


def reset_character(character_name):
    delete_character(character_name, echo=False)

    game_map = gamemap.GameMap(character_name)
    save_game(game_map, echo=False)
    print("Reset {}.".format(character_name))


def create_character():
    name_set = False

    while not name_set:
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
    os.remove(get_saves_dir() + character_name.lower() + ".dat")

    if echo:
        print("Deleted {}.".format(character_name))


def load_options():
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

            if parts[0] == "new":
                return create_character()

            elif parts[0] == "load":
                if len(parts) == 2:
                    return load_game(character_names[parts[1]].lower())
                else:
                    print("Load what?")

            elif parts[0] == "reset":
                if len(parts) == 2:
                    reset_character(character_names[parts[1]])
                else:
                    print("Reset what?")

            elif parts[0] == "delete":
                if len(parts) == 2:
                    delete_character(character_names[parts[1]])
                    break
                else:
                    print("Delete what?")

            else:
                print("Invalid command!")
