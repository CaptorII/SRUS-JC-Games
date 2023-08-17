import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):
    def runTest(self):
        list1 = PlayerList()
        player1 = Player('1', 'john')
        node1 = PlayerNode(player1, None)
        player2 = Player('abc', 'jake')
        node2 = PlayerNode(player2, None)

        self.assertTrue(list1.is_empty)
        list1.add_node_to_head(node1)
        self.assertEqual(list1._start.get_key(), node1.get_key())
        self.assertFalse(list1.is_empty)
        self.assertEqual(list1.get_tail(), node1)
        list1.add_node_to_head(node2)
        self.assertEqual(list1._start.get_key(), node2.get_key())
        self.assertFalse(list1.is_empty)
        self.assertEqual(list1.get_tail(), node1)


if __name__ == '__main__':
    unittest.main()
