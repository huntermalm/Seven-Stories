import unittest
from SevenStories import parse


class TestParse(unittest.TestCase):

    def setUp(self):
        """Set up for all the tests

        Creates a sample command.
        """
        self.sample_command = "health name"

    def test_parse_command(self):
        """Testing parse_command function

        Takes a sample command and returns a sample load.
        Checks that the load is constructed properly.
        """
        sample_load = parse.parse_command(self.sample_command)
        self.assertIs(type(sample_load), list)
        for item in sample_load:
            self.assertIs(type(item), tuple)

    def test_remove_punctuation(self):
        """Testing remove_punctuation function

        Takes a messy command and returns the command
        without punctuation.  Checking that the punctuation is
        removed properly.
        """
        messy_command = "?.display .my health, and !name!"
        clean_command = parse.remove_punctuation(messy_command)
        self.assertEqual(clean_command, "display my health and name")
