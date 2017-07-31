"""Module to isolate the class GameMap"""


import player


class GameMap:

    """Class to define the attributes and behaviors of a gamemap

    The GameMap stores the Player instance.

    +---------------------+----------+------------------------------------------+
    | Instance Attributes | Type     | Description                              |
    +=====================+==========+==========================================+
    | just_saved          | boolean  | True/False is previous action was "save" |
    +---------------------+----------+------------------------------------------+
    | player              | Player   | Instance of the Player                   |
    +---------------------+----------+------------------------------------------+

    :param str name: Name to assign to the Player instance

    """

    def __init__(self, name):
        self.version = "0.1.1"
        self.just_saved = False
        self.player = player.Player(name)
