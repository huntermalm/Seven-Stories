import game


def main():
    game_map = game.load_options()
    print("--------------------------------------------")
    arg = game.play_game(game_map)

    if arg == "quit":
        return


if __name__ == "__main__":
    main()
