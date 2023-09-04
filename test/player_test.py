import unittest
from argon2.exceptions import VerifyMismatchError
from app.player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.players = [Player('1', 'john'), Player('abc', 'jake'), Player('arbys', 'arby')]
        self.players[0].add_password('12345')

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


if __name__ == '__main__':
    unittest.main()
