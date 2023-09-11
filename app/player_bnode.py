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
