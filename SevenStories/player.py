"""Module to isolate the class Player"""


class Player:

    """Class to define the attributes and behaviors of a player

    +---------------------+-----------------+-----------------------+
    | Instance Attributes | Type            | Description           |
    +=====================+=================+=======================+
    | name                | str             | Name set by parameter |
    +---------------------+-----------------+-----------------------+
    | health              | int             | Health (default=100)  |
    +---------------------+-----------------+-----------------------+
    | location            | class Location  | Player's location     |
    +---------------------+-----------------+-----------------------+

    :param str name: Name to assign to Player instance
    :param start_location: Location to initially assign to player instance
    :type start_location: class Location

    """

    def __init__(self, name, start_location):
        self.name = name
        self.health = 100
        self.location = start_location
