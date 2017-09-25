"""Lists of words to be recognized while parsing the user's command

Contains the following lists:
    * actions
    * adjectives
    * locations
    * items
    * containers

"""
filter_words = "the a an my display and to".split()

actions = "health location name save quit go move goto".split()

adjectives = "red green blue first second".split()

locations = ["room"]

items = "phone laptop".split()

containers = "chest backpack table desk bag".split()
