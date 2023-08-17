from __future__ import annotations
from typing import Optional
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._start: Optional[PlayerNode] = None
        self._tail: Optional[PlayerNode] = None
        self.is_empty: bool = True

    def add_node_to_head(self, new_node: PlayerNode):
        if self.is_empty:
            self._start = new_node
            self._tail = new_node
            self.is_empty = False
            return
        temp_node = self._start
        self._start = new_node
        self._start._next_node = temp_node

    def add_node_to_tail(self, new_node: PlayerNode):
        if self.is_empty:
            self._start = new_node
            self._tail = new_node
            self.is_empty = False
            return
        temp_node = self._tail
        self._tail = new_node
        self._tail._prev_node = temp_node

    @property
    def get_head(self) -> PlayerNode:
        return self._start

    @property
    def get_tail(self) -> PlayerNode:
        return self._tail

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}()'
