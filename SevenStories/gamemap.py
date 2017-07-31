"""Module to isolate the class GameMap"""


import player
import locations


class GameMap:

    """Class to define the attributes and behaviors of a gamemap

    The GameMap stores the Player instance and defines a single location
    called "First room"

    +---------------------+----------------+------------------------------------------+
    | Instance Attributes | Type           | Description                              |
    +=====================+================+==========================================+
    | version             | string         | Version of the game                      |
    +---------------------+----------------+------------------------------------------+
    | just_saved          | boolean        | True/False is previous action was "save" |
    +---------------------+----------------+------------------------------------------+
    | locations           | list           | List of all location objects             |
    +---------------------+----------------+------------------------------------------+
    | first_room          | class Location | Temporary first room for the player      |
    +---------------------+----------------+------------------------------------------+
    | player              | Player         | Instance of the Player                   |
    +---------------------+----------------+---------------------------------------

    :param str name: Name to assign to the Player instance

    """

    def __init__(self, name):
        self.version = "0.1.1"
        self.just_saved = False
        self.locations = []

        # Location initializations
        self.first_room = locations.Location("First room")

        # Location appendages
        self.locations.append(self.first_room)

        # Create the player
        self.player = player.Player(name, self.first_room)
