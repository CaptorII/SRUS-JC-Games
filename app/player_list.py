from __future__ import annotations
from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._start = None
        self.is_empty = True        

    def add_node_to_head(self, node: PlayerNode):
        if(self.is_empty):
            self._start = node
            self.is_empty = False
            return
        # else: set node which is currently 'start' as next_node of new node
