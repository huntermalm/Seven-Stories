import unittest
from SevenStories import game


class TestSomething(unittest.TestCase):
    def test_something(self):
        game_map = game.load_game("hunter")
