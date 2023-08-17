import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):
    def runTest(self):
        list1 = PlayerList()
        player1 = Player('1', 'john')
        node1 = PlayerNode(player1)
        player2 = Player('abc', 'jake')
        node2 = PlayerNode(player2)
        player3 = Player('xyz', 'allan')
        node3 = PlayerNode(player3)

        list1.pop_head()  # confirm does not crash if empty
        list1.pop_tail()  # ^
        self.assertTrue(list1.is_empty)
        list1.add_node_to_head(node1)
        self.assertEqual(list1._start.get_key, node1.get_key)
        self.assertFalse(list1.is_empty)
        self.assertEqual(list1.get_tail, node1)
        list1.add_node_to_head(node2)
        self.assertEqual(list1._start.get_key, node2.get_key)
        self.assertFalse(list1.is_empty)
        self.assertEqual(list1.get_tail, node1)
        list1.add_node_to_tail(node3)
        self.assertEqual(list1.get_tail, node3)
        self.assertEqual(list1.get_head, node2)
        list1.pop_tail()
        self.assertEqual(list1.get_tail, node1)
        list1.pop_head()
        self.assertEqual(list1.get_head, node1)
        list1.pop_head()
        self.assertTrue(list1.is_empty)
        list1.add_node_to_tail(node1)
        list1.add_node_to_tail(node2)
        list1.add_node_to_tail(node3)
        list1.pop_key('abc')
        self.assertEqual(list1.get_head.get_next_node, list1.get_tail)
        self.assertEqual(list1.get_tail, node3)


if __name__ == '__main__':
    unittest.main()