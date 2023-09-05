from __future__ import annotations
from typing import MutableSequence
from random import shuffle
from argon2 import PasswordHasher
ph = PasswordHasher()


class Player:
    """A Player object holds information about users"""
    def __init__(self, uid: str, name: str):
        self._uid: str = uid
        self._name: str = name
        self._hashed_password: str | None = None
        self._score: int = 0

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    def add_password(self, new_password: str):
        self._hashed_password = ph.hash(new_password)

    def verify_password(self, password_guess: str = None) -> bool:
        if password_guess is None:
            raise TypeError("No password provided")
        if self._hashed_password is None:
            raise TypeError("No password on account")
        return ph.verify(self._hashed_password, password_guess)

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int):
        if value > 0:
            self._score = value

    # just shuffles and checks if sorted, repeats until sorted
    def bogosort_players(self, list_of_players: MutableSequence[Player]) -> None:
        shuffle(list_of_players)
        if not self.verify_sort(list_of_players):
            self.bogosort_players(list_of_players)

    # actually sorts so we have something to verify against
    @staticmethod
    def verify_sort(sorted_list: MutableSequence[Player]) -> bool:
        verification_list = sorted_list[:]
        # sort verification_list using bubble sort
        for index, current_player in enumerate(verification_list):
            if index + 1 == len(verification_list):
                break
            if current_player < verification_list[index + 1]:
                verification_list[index] = verification_list[index + 1]
                verification_list[index + 1] = current_player
        return sorted_list == verification_list

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(uid= {self._uid}, name= {self._name}, score= {self._score})'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(uid={self._uid!r}, name={self._name!r}, hashed password= {self._hashed_password}' \
               f', score= {self._score!r})'

    def __eq__(self, other):
        return self._score == other.score

    def __ge__(self, other):
        return self._score >= other.score

    def __le__(self, other):
        return self._score <= other.score

    def __lt__(self, other):
        return self._score < other.score

    def __gt__(self, other):
        return self._score > other.score
