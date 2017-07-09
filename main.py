import game


RUNNING = True
while RUNNING:
    game_map = game.load_options()
    print("--------------------------------------------")
    arg = game.play_game(game_map)

    if arg == "quit":
        RUNNING = False
