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
    | locations           | list    | List of all location objects             |
    +---------------------+---------+------------------------------------------+
    | player              | Player  | Instance of the Player                   |
    +---------------------+---------+------------------------------------------+

    :param str name: Name to assign to the Player instance

    """

    def __init__(self, name):
        self.version = "0.2.0"
        self.just_saved = False
        self.locations = []

        # Location appendages
        self.locations.append(locations.Location("First room"))

        # Create the player
        self.player = player.Player(name, self.get_location("First room"))

    def get_location(self, location_name):
        for location in self.locations:
            if location.name == location_name:
                return location
