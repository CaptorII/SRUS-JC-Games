import random
import unittest
from app.player import Player
from app.player_list import PlayerList


class PlayerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.list1 = PlayerList()
        random_list = random.sample(range(100), 10)
        names_list = ['john', 'jack', 'allan', 'jane', 'eliza', 'andrew', 'lewis', 'joe', 'beth', 'adam']
        self.players = [Player(uid, names_list[index % len(names_list)])
                        for index, uid in enumerate(random_list)]

    def test_list_is_empty_property(self):
        self.assertTrue(self.list1.is_empty)
        self.list1.add_node_to_tail(self.players[0])
        self.assertFalse(self.list1.is_empty)

    def test_adding_to_head(self):
        self.list1.add_node_to_head(self.players[0])
        self.assertFalse(self.list1.is_empty)
        self.assertIs(self.list1.head.player, self.players[0])
        self.list1.add_node_to_head(self.players[1])
        self.assertIs(self.list1.head.player, self.players[1])

    def test_adding_to_tail(self):
        self.list1.add_node_to_tail(self.players[0])
        self.list1.add_node_to_tail(self.players[1])
        self.list1.add_node_to_tail(self.players[2])
        self.assertIs(self.list1.tail.player, self.players[2])
        self.assertIs(self.list1.head.player, self.players[0])

    def test_removing_from_tail(self):
        self.list1.add_node_to_tail(self.players[0])
        self.list1.add_node_to_tail(self.players[1])
        self.list1.pop_tail()
        self.assertIs(self.list1.tail.player, self.players[0])

    def test_removing_from_head(self):
        self.list1.add_node_to_tail(self.players[0])
        self.list1.add_node_to_tail(self.players[1])
        self.list1.pop_head()
        self.assertIs(self.list1.head.player, self.players[1])
        self.list1.pop_head()
        self.assertTrue(self.list1.is_empty)

    def test_removing_by_key(self):
        self.list1.add_node_to_tail(self.players[0])
        self.list1.add_node_to_tail(self.players[1])
        self.list1.add_node_to_tail(self.players[2])
        self.list1.pop_key(self.players[1].uid)  # pop node from middle
        self.assertEqual(self.list1.head.next_node, self.list1.tail)
        self.assertEqual(self.list1.tail.player, self.players[2])
        self.list1.pop_key(self.players[0].uid)  # pop node from head
        self.assertEqual(self.list1.head, self.list1.tail)
        self.list1.pop_key(self.players[2].uid)  # pop final node so list is empty
        self.assertTrue(self.list1.is_empty)

    def test_displaying_list(self):
        self.list1.display(True)
        self.list1.add_node_to_tail(self.players[0])
        self.list1.add_node_to_tail(self.players[1])
        self.list1.add_node_to_tail(self.players[2])
        self.list1.display()
        self.list1.display(False)


if __name__ == '__main__':
    unittest.main()
