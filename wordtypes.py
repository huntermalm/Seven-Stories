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


class Preposition(Word):

    def __init__(self, word, index):
        super().__init__(word, index)


class Pronoun(Word):

    def __init__(self, word, index):
        super().__init__(word, index)
