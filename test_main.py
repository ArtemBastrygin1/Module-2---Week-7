import unittest
from main import TreasureMap, Player, Game


class TestTreasureMap(unittest.TestCase):
    def test_generate_treasure_location(self):
        treasure_map = TreasureMap()
        size = treasure_map.size
        treasure_location = treasure_map.generate_treasure_location()
        self.assertTrue(0 <= treasure_location[0] < size)
        self.assertTrue(0 <= treasure_location[1] < size)

    def test_is_treasure_at(self):
        treasure_map = TreasureMap()
        treasure_map.treasure_location = (5, 5)
        self.assertTrue(treasure_map.is_treasure_at(5, 5))
        self.assertFalse(treasure_map.is_treasure_at(4, 4))

    def test_get_hint(self):
        treasure_map = TreasureMap()
        treasure_map.treasure_location = (5, 5)
        self.assertEqual(treasure_map.get_hint(5, 5), "Поздравляем! Вы выиграли сокровище!")
        self.assertEqual(treasure_map.get_hint(6, 6), "Вы очень близко к сокровищу!")
        self.assertEqual(treasure_map.get_hint(8, 8), "Вы далеко от сокровища!")


class TestPlayer(unittest.TestCase):
    def test_make_guess(self):
        player = Player("TestPlayer")
        guess = (3, 4)
        player.make_guess(guess)
        self.assertEqual(player.guesses, [guess])
        self.assertEqual(player.attempts, 1)


class TestGame(unittest.TestCase):
    def test_game_over(self):
        player = Player("TestPlayer")
        treasure_map = TreasureMap()
        treasure_map.treasure_location = (0, 0)
        game = Game(player, treasure_map)
        game.play()
        self.assertTrue(player.attempts > 0)


if __name__ == "__main__":
    unittest.main()
