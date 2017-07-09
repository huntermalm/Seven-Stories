import player


class GameMap:

    def __init__(self, name):
        self.just_saved = False
        self.player = player.Player(name)
