from actions import get_action_dictionary
import wordtypes
import lists


def parse_command(command):
    load = []
    raw_parts = remove_punctuation(command).split()

    action_objects = [wordtypes.Action(word, index)
                      for index, word in enumerate(raw_parts)
                      if word in lists.actions]

    adjective_objects = [wordtypes.Adjective(word, index)
                         for index, word in enumerate(raw_parts)
                         if word in lists.adjectives]

    for action_object in action_objects:
        for str_action, function in get_action_dictionary().items():
            if action_object.word == str_action:
                load.append((function, action_object))

    return load


def remove_punctuation(command):
    punctuation = [".", ",", "!", "'", '"', "?"]

    cmd_characters = list(command)
    new_cmd_characters = [cmd_character
                          for cmd_character in cmd_characters
                          if cmd_character not in punctuation]

    new_command = "".join(new_cmd_characters)

    return new_command
