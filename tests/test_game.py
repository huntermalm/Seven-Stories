import unittest
from SevenStories import game
from SevenStories import parse


class TestGame(unittest.TestCase):

    def setUp(self):
        """Set up for all the tests

        Creates a sample character and stores the GameMap object.
        Creates a sample load with 'health name' as sample input.
        """
        self.sample_input = "health name"
        self.sample_name = "testcharacter"
        self.game_map = game.create_character(lambda x: "test")
        self.load = parse.parse_command(self.sample_input)

    def tearDown(self):
        import os

        os.remove(game.get_saves_dir() + self.game_map.player.name.lower() + ".dat")

    def test_play_game(self):
        """Testing play_game function

        Using 'save quit' as example input.
        Expecting play_game to not only run successfully, but in this case,
        it should also return 'quit', which will be stored as arg.
        If this test passes, then the execute function's arg return works.
        """
        arg = game.play_game(self.game_map, input=lambda x: "save quit")
        self.assertEqual(arg, "quit", "Arg was not quit!")

    def test_execute(self):
        """Testing execute function

        Sample load uses 'health name' as example input
        Simply testing to ensure the function runs successfully.
        """
        game.execute(self.game_map, self.load)

    def test_get_saves_dir(self):
        import os
        """Testing get_saves_dir function

        The project directory is expected to contain the saves directory,
        just as 'Seven Stories/saves'.  This test will check the returned
        absolute path from the get_saves_dir function and ensure that
        the ending is 'Seven Stories/saves'.

        Test handles differences between how operating systems handle
        slashes in directory paths.
        """
        saves_dir = game.get_saves_dir()

        if os.name == "posix":
            self.assertEqual(saves_dir[len(saves_dir) - 20:],
                             "Seven Stories/saves/",
                             "Incorrect saves directory returned!")
        else:
            self.assertEqual(saves_dir[len(saves_dir) - 20:],
                             "Seven Stories\\saves\\",
                             "Incorrect saves directory returned!")

    def test_get_simple_answer(self):
        """Testing get_simple_answer function

        Running the two most important sample answers, 'yes' and 'no'.
        """

        answer1 = game.get_simple_answer("Test question.", input=lambda x: "yes")
        answer2 = game.get_simple_answer("Test question.", input=lambda x: "no")

        self.assertTrue(answer1, "First answer failed to return True!")
        self.assertFalse(answer2, "Second answer failed to return False!")

    def test_save_game(self):
        """Testing save_game function

        Simply testing to ensure the function runs successfully.
        """
        game.save_game(self.game_map, echo=False)

    def test_load_game(self):
        """Testing load_game function

        Ensuring that load_game returns a GameMap object
        and ensuring that the correct game_map is loaded
        by checking the player's name within it.
        """
        sample_game_map = game.load_game("test")
        self.assertIsInstance(sample_game_map, game.gamemap.GameMap,
                              "Did not return a GameMap object!")
        self.assertEqual(sample_game_map.player.name, "test",
                         "Failed to load the correct GameMap object!")

    def test_reset_character(self):
        """Testing reset_character function

        Simply testing to ensure the function runs successfully.
        """
        game.reset_character("test", echo=False)

    def test_create_character(self):
        """Testing create_character function

        Creating a sample character with sample name.
        Ensuring that create_character returns the proper GameMap object

        Deletes the sample character after
        """
        sample_game_map = game.create_character(input=lambda x: self.sample_name)

        self.assertIsInstance(sample_game_map, game.gamemap.GameMap,
                              "Did not return a GameMap object!")
        self.assertEqual(sample_game_map.player.name, self.sample_name,
                         "Failed to create the correct GameMap object!")
        game.delete_character(sample_game_map.player.name, echo=False)

    def test_delete_character(self):
        """Testing delete_character function

        Creating a sample character with sample name.
        Deleting that character after it's created.
        Checking directory to ensure that the character does not exist.
        """
        sample_game_map = game.create_character(input=lambda x: self.sample_name)

        game.delete_character(sample_game_map.player.name.lower(), echo=False)
