import unittest
from SevenStories import game
from SevenStories import parse


class TestActions(unittest.TestCase):

    def setUp(self):
        """Set up for all the tests

        Creates sample name for sample character.
        Creates a sample character and stores the GameMap object.
        """
        self.sample_name = "testcharacter"
        self.sample_game_map = game.create_character(lambda x: self.sample_name)
        self.sample_command = "name health save quit"

    def tearDown(self):
        game.delete_character(self.sample_game_map.player.name, echo=False)

    def test_actions(self):
        """Testing all actions

        The game's core functionality provide a good set of tools that will
        allow this test to setup everything it needs very easily, assuming
        that they work properly.  By passing a command with every possible
        action into the command parser, a load will be constructed with all
        of those actions.  The load is tested by passing it to the execute
        function.
        """
        load = parse.parse_command(self.sample_command)
        game.execute(self.sample_game_map, load)
