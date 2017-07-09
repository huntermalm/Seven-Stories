def name(game_map, action_object):
    print("Name: {}".format(game_map.player.name))


def health(game_map, action_object):
    print("Health: {}%".format(game_map.player.health))


def save(game_map, action_object):
    from game import save_game
    save_game(game_map)


def quit(game_map, action_object):
    if not game_map.just_saved:
        response = input("Would you like to save before quitting (y\\n)? ").lower()
        print("--------------------------------------------")
        if response[0] == 'y':
            save(game_map, action_object)
            print("--------------------------------------------")

    print("Quitting..\n")

    return "quit"


def get_action_dictionary():
    action_dictionary = {
        "name": name, "health": health, "save": save, "quit": quit
        }

    return action_dictionary
