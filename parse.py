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

    get_full_objects(adjective_objs, object_objs)

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

    [print("{} at {}".format(full_object.word, full_object.index)) for full_object in full_objects]

    return full_objects
