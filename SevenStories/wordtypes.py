"""Stores all of the different word classes

The base Word class is inherited by all of the other classes.  It contains
the logic to store the string of the word in particular, as well of the index
of where that word appeared in the user's command.

Any instance of any of these classes can be referred to as a word object,
however, an action word object can be simplified as just an action object.

"""


class Word:

    """Class to define the attributes and behaviors of a generic word object

    +---------------------+------+---------------------------------+
    | Instance Attributes | Type | Description                     |
    +=====================+======+=================================+
    | word                | str  | Recognized word                 |
    +---------------------+------+---------------------------------+
    | index               | int  | Index of word in user's command |
    +---------------------+------+---------------------------------+

    """

    def __init__(self, word, index):
        self.word = word
        self.index = index


class Action(Word):

    """Class to define the attributes and behaviors of an action object"""

    def __init__(self, word, index):
        super().__init__(word, index)


class Object(Word):

    """Class to define the attributes and behaviors of an action object"""

    def __init__(self, word, index, object_type):
        super().__init__(word, index)
        self.adjectives = []
        self.type = object_type

    def get_fullname(self):
        if self.adjectives:
            return "".join([adj.word + " " for adj in self.adjectives]) + self.word

        else:
            return self.word


class Adjective(Word):

    """Class to define the attributes and behaviors of an adjective object"""

    def __init__(self, word, index):
        super().__init__(word, index)


class Preposition(Word):

    """Class to define the attributes and behaviors of a preposition object"""

    def __init__(self, word, index):
        super().__init__(word, index)


class Pronoun(Word):

    """Class to define the attributes and behaviors of a pronoun object"""

    def __init__(self, word, index):
        super().__init__(word, index)
