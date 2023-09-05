import unittest
from argon2.exceptions import VerifyMismatchError
from app.player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.players = [Player('1', 'john'), Player('abc', 'jake'), Player('arbys', 'arby'), Player('15', 'adam'),
                        Player('2', 'zac')]
        self.players[0].add_password('12345')
        self.players[0].score = 5
        self.players[1].score = 10
        self.players[2].score = 15
        self.players[3].score = 10

    def test_player_creation(self):
        self.assertEqual(self.players[0].uid, '1')
        self.assertEqual(self.players[1].name, 'jake')
        self.assertEqual(self.players[2].uid, 'arbys')

    def test_password_is_incorrect(self):
        with self.assertRaises(VerifyMismatchError):
            self.players[0].verify_password('54321')
            self.players[0].verify_password('1234')
            self.players[0].verify_password('password')

    def test_password_is_correct(self):
        self.assertTrue(self.players[0].verify_password('12345'))

    def test_no_password_passed(self):
        with self.assertRaises(TypeError):
            self.players[0].verify_password()

    def test_score_comparisons(self):
        self.assertTrue(self.players[0] < self.players[1])
        self.assertTrue(self.players[2] > self.players[0])
        self.assertTrue(self.players[3] >= self.players[1])
        self.assertFalse(self.players[2] <= self.players[1])
        self.assertEqual(self.players[1], self.players[3])

    def test_bogosort(self):
        verification_set = self.players[:]
        verification_set.sort(key=None, reverse=True)
        self.players[0].bogosort_players(self.players)
        self.assertEqual(self.players, verification_set)


if __name__ == '__main__':
    unittest.main()
