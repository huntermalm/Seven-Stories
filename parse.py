from actions import get_action_dictionary
import wordtypes
import lists


def parse_command(command):
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

    load = [(get_action_dictionary()[action_object.word], action_object)
            for action_object in action_objs]

    return load


def remove_punctuation(command):
    punctuation = [".", ",", "!", "'", '"', "?"]

    cmd_characters = list(command)
    new_cmd_characters = [cmd_character
                          for cmd_character in cmd_characters
                          if cmd_character not in punctuation]

    new_command = "".join(new_cmd_characters)

    return new_command
