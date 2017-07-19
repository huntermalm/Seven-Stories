"""Module to isolate the class Player"""


class Player:

    """Class to define the attributes and behaviors of a player

    +---------------------+------+-----------------------+
    | Instance Attributes | Type | Description           |
    +=====================+======+=======================+
    | name                | str  | Name set by parameter |
    +---------------------+------+-----------------------+
    | health              | int  | Health (default=100)  |
    +---------------------+------+-----------------------+

    :param str name: Name to assign to Player instance

    """

    def __init__(self, name):
        self.name = name
        self.health = 100
