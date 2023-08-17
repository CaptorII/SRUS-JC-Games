from __future__ import annotations
from typing import Optional
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._start: Optional[PlayerNode] = None
        self.is_empty: bool = True

    def add_node_to_head(self, new_node: PlayerNode):
        if self.is_empty:
            self._start = new_node
            self.is_empty = False
            return
        temp_node = self._start
        self._start = new_node
        self._start._next_node = temp_node
