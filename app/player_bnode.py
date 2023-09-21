from __future__ import annotations
from app.player import Player


class PlayerBNode:
    def __init__(self, player: Player):
        self._value = player
        self._left: PlayerBNode | None = None
        self._right: PlayerBNode | None = None

    @property
    def value(self) -> Player:
        return self._value

    @property
    def left(self) -> PlayerBNode | None:
        return self._left

    @left.setter
    def left(self, node: PlayerBNode) -> None:
        self._left = node

    @property
    def right(self) -> PlayerBNode | None:
        return self._right

    @right.setter
    def right(self, node: PlayerBNode) -> None:
        self._right = node

    @property
    def is_leaf(self) -> bool:
        return self._left is None and self._right is None

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(player= {self._value})"

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(player={self._value!r}, left={self._left!r}, right={self._right!r})"

    def __eq__(self, other):
        return self._value.name == other.value.name

    def __ge__(self, other):
        return self._value.name >= other.value.name

    def __le__(self, other):
        return self._value.name <= other.value.name

    def __lt__(self, other):
        return self._value.name < other.value.name

    def __gt__(self, other):
        return self._value.name > other.value.name
