import unittest
from app.player import Player


class PlayerTest(unittest.TestCase):
    def runTest(self):
        player1 = Player('1', 'john')
        player2 = Player('abc', 'jake')
        player3 = Player('arbys', 'arby')
        self.assertEqual(player1.get_uid, '1')
        self.assertEqual(player2.get_name, 'jake')
        self.assertEqual(player3.get_uid, 'arbys')


if __name__ == '__main__':
    unittest.main()

