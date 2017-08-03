"""Module to isolate the class GameMap"""


import player
import locations


class GameMap:

    """Class to define the attributes and behaviors of a gamemap

    The GameMap stores the Player instance and defines a single location
    called "First room"

    +---------------------+---------+------------------------------------------+
    | Instance Attributes | Type    | Description                              |
    +=====================+=========+==========================================+
    | version             | string  | Version of the game                      |
    +---------------------+---------+------------------------------------------+
    | just_saved          | boolean | True/False is previous action was "save" |
    +---------------------+---------+------------------------------------------+
    | locations           | dict    | List of all location objects             |
    +---------------------+---------+------------------------------------------+
    | player              | Player  | Instance of the Player                   |
    +---------------------+---------+------------------------------------------+

    :param str name: Name to assign to the Player instance

    """

    def __init__(self, name):
        self.version = "0.3.0"
        self.just_saved = False
        self.locations = {}

        # Location appendages
        self.locations["first room"] = locations.Location("First room")
        self.locations["second room"] = locations.Location("Second room")

        # Location connections
        self.locations["first room"].available_locations["second room"] = self.locations["second room"]
        self.locations["second room"].available_locations["first room"] = self.locations["first room"]

        # Create the player
        self.player = player.Player(name, self.locations["first room"])
