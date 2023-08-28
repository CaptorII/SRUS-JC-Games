import unittest
from app.player import Player


class PlayerTest(unittest.TestCase):
    def test_players(self):
        player1 = Player('1', 'john')
        player2 = Player('abc', 'jake')
        player3 = Player('arbys', 'arby')
        self.assertEqual(player1.uid, '1')
        self.assertEqual(player2.name, 'jake')
        self.assertEqual(player3.uid, 'arbys')


if __name__ == '__main__':
    unittest.main()
