import random
import unittest
from app.player import Player
from app.player_bst import PlayerBST


class PlayerBSTTest(unittest.TestCase):
    def setUp(self) -> None:
        random_list = random.sample(range(100), 10)
        names_list = ['john', 'jack', 'allan', 'jane', 'eliza', 'andrew', 'lewis', 'joe', 'beth', 'adam']
        self.players = [Player(uid, names_list[index % len(names_list)])
                        for index, uid in enumerate(random_list)]
        self.tree = PlayerBST(self.players[0])

    def test_inserting_players(self):
        self.tree.insert(self.players[1])
        self.tree.insert(self.players[2])
        self.tree.insert(self.players[3])
        self.assertFalse(self.tree.root.is_leaf)
        self.assertIs(self.tree.root.left.value, self.players[1])
        self.assertIs(self.tree.root.left.left.value, self.players[2])
        self.assertIs(self.tree.root.left.right.value, self.players[3])


if __name__ == '__main__':
    unittest.main()
