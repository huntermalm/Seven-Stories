Contains functions designed to parse user's input specifically for the game.
This game supports multiple commands at a time.  To prevent any confusion,
a convention must be set.  For this game, any word that the user can enter
that causes something to happen is called an action.  A user's command may
contain an unlimited amount of actions.

To ensure control over the user's capabilities, a set of lists from lists.py
are imported.  These lists contain the words that are recognized during
parsing.  The parse_command() function will only create word objects with the
words that appear in both the user's command and any of the lists.
"""


from actions import get_action_dictionary
import wordtypes
import lists


def parse_command(command):
    """Parse a user's command and return a load

    The load is a list of tuples each containing a function and action object.
    to construct a load.

    This starts with removing any punctuation from the user's command, and then
    splitting the words up into a list of raw parts.

    By using list comprehension, the words in the raw parts list is iterated
    over and checked to see if it appears in a particular list.  If the word
    example, if the user's command contained the word "blue", it would appear
    inside the raw parts list.  When iterating over that list, this function
    will recognize it as an adjective, and create an adjective word object,
    storing the word itself and the index of that word.  This adjective word
    object would then be stored in a list of adjective word objects.  A list of
    word objects is created for every type of word.

    The load is constructed by iterating over the action word objects in the
    action objects list.  For every action object in the list, a new tuple is
    created storing two values.  The first value is a function obtained
    by passing the word within the action object to a dictionary obtained
    through the get_action_dictionary() function in actions.py.  The second
    value is the action object itself, useful for storing the direct objects
    and objects of prepositions.  Once fully constructed, the load is returned.

    :param str command: Command to parse
    :return: List of tuples formatted as (function, action_object)
    :rtype: List

    """
    raw_parts = remove_punctuation(command).split()

    action_objs = [wordtypes.Action(word, index)
                   for index, word in enumerate(raw_parts)
                   if word in lists.actions]

    adjective_objs = [wordtypes.Adjective(word, index)
                      for index, word in enumerate(raw_parts)
                      if word in lists.adjectives]

    object_objs = [wordtypes.Object(word, index, "item")
                   for index, word in enumerate(raw_parts)
                   if word in lists.items]
    object_objs.extend([wordtypes.Object(word, index, "location")
                        for index, word in enumerate(raw_parts)
                        if word in lists.locations])
    object_objs.extend([wordtypes.Object(word, index, "container")
                        for index, word in enumerate(raw_parts)
                        if word in lists.containers])

    get_full_objects(adjective_objs, object_objs)

    load = [(get_action_dictionary()[action_object.word], action_object)
            for action_object in action_objs]

    return load


def remove_punctuation(command):
    """Takes in a command and returns it with removed punctuation

    :param str command: Command to remove punctuation from
    :return: Command without punctuation
    :rtype: str

    """
    punctuation = [".", ",", "!", "'", '"', "?"]

    cmd_characters = list(command)
    new_cmd_characters = [cmd_character
                          for cmd_character in cmd_characters
                          if cmd_character not in punctuation]

    new_command = "".join(new_cmd_characters)

    return new_command


def get_full_objects(adjective_objs, object_objs):
    combined_list = []
    combined_list.extend(adjective_objs)
    combined_list.extend(object_objs)
    combined_list.sort(key=lambda word_obj: word_obj.index)

    adj_indexes = [adj_obj.index for adj_obj in adjective_objs]

    adjectives = []
    full_objects = []

    for word_obj in combined_list:
        if word_obj.index in adj_indexes:
            adjectives.append(word_obj)
        elif adjectives:
            if adjectives[len(adjectives) - 1].index == word_obj.index - 1:
                full_object_name = "".join([adj.word + " " for adj in adjectives]) + word_obj.word
                full_objects.append(wordtypes.FullObject(full_object_name, word_obj))
                adjectives = []
            else:
                full_objects.append(wordtypes.FullObject(word_obj.word, word_obj))
                adjectives = []
        else:
            full_objects.append(wordtypes.FullObject(word_obj.word, word_obj))
            adjectives = []

    # [print("{} at {}".format(full_object.word, full_object.index)) for full_object in full_objects]

    return full_objects
