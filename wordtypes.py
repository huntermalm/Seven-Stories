class Word:

    def __init__(self, word, index):
        self.word = word
        self.index = index


class Action(Word):

    def __init__(self, word, index):
        super().__init__(word, index)


class Adjective(Word):

    def __init__(self, word, index):
        super().__init__(word, index)


class Object(Word):

    def __init__(self, word, index, object_type):
        super().__init__(word, index)
        self.type = object_type


class Preposition(Word):

    def __init__(self, word, index):
        super().__init__(word, index)


class Pronoun(Word):

    def __init__(self, word, index):
        super().__init__(word, index)
