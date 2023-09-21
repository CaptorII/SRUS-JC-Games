import random
import unittest
from app.player import Player
from app.player_bst import PlayerBST


class PlayerBSTTest(unittest.TestCase):
    def setUp(self) -> None:
        random_list = random.sample(range(100), 10)
        self.names_list = ['john', 'jack', 'allan', 'jane', 'eliza', 'andrew', 'lewis', 'joe', 'beth', 'adam']
        self.players = [Player(uid, self.names_list[index % len(self.names_list)])
                        for index, uid in enumerate(random_list)]
        self.tree = PlayerBST(self.players[0])
        self.tree.insert(self.players[1])
        self.tree.insert(self.players[2])
        self.tree.insert(self.players[3])

    def test_inserting_players(self):
        self.assertFalse(self.tree.root.is_leaf)
        self.assertIs(self.tree.root.left.value, self.players[1])
        self.assertIs(self.tree.root.left.left.value, self.players[2])
        self.assertIs(self.tree.root.left.right.value, self.players[3])

    def test_searching_tree(self):
        self.assertEqual(self.tree.search(self.names_list[0]), self.tree.root)
        self.assertEqual(self.tree.search(self.names_list[1]), self.tree.root.left)
        self.assertEqual(self.tree.search(self.names_list[3]), self.tree.root.left.right)


if __name__ == '__main__':
    unittest.main()
