"""Provide functionality to parse user input

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
    The goal of this function is to build all of the necessary pieces required
    to construct a load.

    This starts with removing any punctuation from the user's command, and then
    splitting the words up into a list of raw parts.

    By using list comprehension, the words in the raw parts list is iterated
    over and checked to see if it appears in a particular list.  If the word
    does appear in a list, a word object specific to that type of word is
    created and then stored into a list of those specific types of objects.  For
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

    add_adjectives_to_objects(adjective_objs, object_objs)

    for action_object in action_objs:
        action_object.direct_objects = get_direct_objects(action_object, object_objs)

        print("DOs for {}: ".format(action_object.word), end="")

        for count, direct_object in enumerate(action_object.direct_objects):
            print(direct_object.get_fullname(), end="")

            if len(action_object.direct_objects) - 1 != count:
                print(", ", end="")

        print()

    load = [(get_action_dictionary()[action_object.word], action_object)
            for action_object in action_objs]

    return load


def get_direct_objects(action_object, object_objs):
    direct_objects = []

    for object_object in object_objs:
        adjective_count = len(object_object.adjectives)
        if object_object.index - adjective_count - 1 == action_object.index:
            direct_objects.append(object_object)

        elif direct_objects:
            if object_object.index - adjective_count - 1 == direct_objects[len(direct_objects) - 1].index:
                direct_objects.append(object_object)

    return direct_objects


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


def add_adjectives_to_objects(adjective_objs, object_objs):
    """Adds adjective objects to object objects

    Not the cleanest function by no means, but it works for now.  The idea
    is to be able to iterate linearly, checking whether the word is an
    adjective or an object, and doing things occordingly.  So first, the
    adjectives and objects are combined into the same list, which is then
    sorted by their index attributes.  This gets them all together in order
    as they appeared originally in the user's command.

    While iterating the combined list, if the word object is an adjective, then
    it gets added to a list of temporary adjectives.  Once the iteration
    reaches an object word object, it checks if the last word in the temporary
    adjectives list appeared before it.  If so, then all of the temporary
    adjectives objects get added to the object object's adjectives attribute
    and the temporary adjectives list is cleared.

    :param adjective_objs: List of adjective word objects
    :type adjective_objs: list
    :param object_objs: List of object word objects
    :type object_objs: list

    """
    combined_list = []
    combined_list.extend(adjective_objs)
    combined_list.extend(object_objs)
    combined_list.sort(key=lambda word_obj: word_obj.index)

    temp_adjs = []

    for word_obj in combined_list:
        if word_obj.word in lists.adjectives:
            temp_adjs.append(word_obj)
        else:
            if temp_adjs:
                if temp_adjs[len(temp_adjs) - 1].index == word_obj.index - 1:
                    word_obj.adjectives = temp_adjs
                    temp_adjs = []

    [print("{} at {} ({} adjectives)".format(object_obj.get_fullname(), object_obj.index, len(object_obj.adjectives))) for object_obj in object_objs]
