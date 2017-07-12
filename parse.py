from actions import get_action_dictionary
import wordtypes
import lists


def parse_command(command):
    raw_parts = remove_punctuation(command).split()

    action_objects = [wordtypes.Action(word, index)
                      for index, word in enumerate(raw_parts)
                      if word in lists.actions]

    adjective_objects = [wordtypes.Adjective(word, index)
                         for index, word in enumerate(raw_parts)
                         if word in lists.adjectives]

    load = [(get_action_dictionary()[action_object.word], action_object)
            for action_object in action_objects]

    return load


def remove_punctuation(command):
    punctuation = [".", ",", "!", "'", '"', "?"]

    cmd_characters = list(command)
    new_cmd_characters = [cmd_character
                          for cmd_character in cmd_characters
                          if cmd_character not in punctuation]

    new_command = "".join(new_cmd_characters)

    return new_command
