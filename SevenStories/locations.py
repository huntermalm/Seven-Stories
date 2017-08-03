"""Module to store the class Location"""


class Location:

    """Class to define the attributes and behaviors of a location

    +---------------------+------+------------------------------------+
    | Instance Attributes | Type | Description                        |
    +=====================+======+====================================+
    | name                | str  | Name set by parameter              |
    +---------------------+------+------------------------------------+
    | available_location  | list | List of available Location objects |
    +---------------------+------+------------------------------------+

    :param str name: Name to assign to Location instance

    """

    def __init__(self, name):
        self.name = name
        self.available_locations = {}
