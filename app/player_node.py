from __future__ import annotations
from typing import Optional
from app.player import Player


class PlayerNode:
    """PlayerNodes are part of a linked list implementation"""
    def __init__(self, player: Player):
        self._player = player
        self._prev_node: Optional[PlayerNode] = None
        self._next_node: Optional[PlayerNode] = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def previous_node(self) -> PlayerNode:
        return self._prev_node

    @previous_node.setter
    def previous_node(self, prev_node: PlayerNode):
        self._prev_node = prev_node

    @property
    def next_node(self) -> PlayerNode:
        return self._next_node

    @next_node.setter
    def next_node(self, next_node: PlayerNode):
        self._next_node = next_node

    @property
    def key(self) -> str:
        return self._player.uid

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(player= {self._player})"

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(player={self._player!r})"
