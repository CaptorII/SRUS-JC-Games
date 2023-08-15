import unittest
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):
    def runTest(self):
        list = PlayerList()
        self.assertEqual(list.get_uid, '1')


if __name__ == '__main__':
    unittest.main()
