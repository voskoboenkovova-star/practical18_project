import unittest
from core.characters import Character
from core.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.char1 = Character("Amber", "Pyro", 4, "resources/characters/amber.png")
        self.char2 = Character("Diluc", "Pyro", 5, "resources/characters/diluc.png")
        self.game = Game([self.char1, self.char2])

    def test_select_character(self):
        self.game.select_character("Amber")
        self.assertEqual(self.game.current_player.name, "Amber")
        self.assertIn("Выбрали персонажа Amber", self.game.history)

    def test_perform_action(self):
        self.game.select_character("Diluc")
        result = self.game.perform_action("атака")
        self.assertIn("Diluc выполняет атака", result)
        self.assertIn(result, self.game.get_history())

    def test_history_empty(self):
        self.assertEqual(self.game.get_history(), [])

if __name__ == "__main__":
    unittest.main()
