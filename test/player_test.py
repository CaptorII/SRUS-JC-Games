import unittest
from app.player import Player


class PlayerTest(unittest.TestCase):
    def test_players(self):
        players = [Player('1', 'john'), Player('abc', 'jake'), Player('arbys', 'arby')]
        self.assertEqual(players[0].uid, '1')
        self.assertEqual(players[1].name, 'jake')
        self.assertEqual(players[2].uid, 'arbys')


if __name__ == '__main__':
    unittest.main()
