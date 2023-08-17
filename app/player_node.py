from __future__ import annotations
from typing import Optional
from app.player import Player


class PlayerNode:
    def __init__(self, player: Player, prev_node: Optional[PlayerNode]):
        self._player = player
        if prev_node:
            self._prev_node = prev_node
        else:
            self._prev_node = None
        self._next_node: Optional[PlayerNode] = None

    def get_player(self) -> Player:
        return self._player

    def get_prev_node(self) -> PlayerNode:
        return self._prev_node

    def get_next_node(self) -> PlayerNode:
        return self._next_node

    def set_next_node(self, next_node: PlayerNode):
        self._next_node = next_node

    def get_key(self) -> str:
        return self._player.get_uid

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(player={self._player}, prev_node={self._prev_node})"

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(player={self._player!r}, prev_node={self._prev_node!r})"
