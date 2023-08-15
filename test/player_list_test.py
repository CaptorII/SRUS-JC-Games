import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):
    def runTest(self):
        list = PlayerList()
        list.add_node_to_head(PlayerNode(Player('1', 'john')))
        self.assertEqual(list._start.get_key, '1')
        list.add_node_to_head(PlayerNode(Player('abc', 'jake')))
        self.assertEqual(list._start.get_key, 'abc')


if __name__ == '__main__':
    unittest.main()
