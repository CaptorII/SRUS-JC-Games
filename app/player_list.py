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
        self._start.next_node = temp_node
        temp_node.prev_node = self._start

    def add_node_to_tail(self, new_node: PlayerNode):
        if self.is_empty:
            self._start = new_node
            self._tail = new_node
            self.is_empty = False
            return
        temp_node = self._tail
        self._tail = new_node
        self._tail.prev_node = temp_node
        temp_node.next_node = self._tail

    def pop_head(self):
        if self.is_empty:
            return
        if self._start.next_node is None:
            self._start = None
            self.is_empty = True
            return
        self._start = self._start.next_node
        self._start.prev_node = None

    def pop_tail(self):
        if self.is_empty:
            return
        if self._tail.prev_node is None:
            self._tail = None
            self.is_empty = True
            return
        self._tail = self._tail.prev_node
        self._tail.next_node = None

    def pop_key(self, key: str):
        if self.is_empty:
            return
        temp_node = self._start
        if temp_node.get_key == key:
            self.pop_head()
            return
        while temp_node.next_node is not None or temp_node is self._tail:
            if temp_node.get_key == key:
                if temp_node.next_node is not None:
                    next = temp_node.next_node
                    prev = temp_node.prev_node
                    next.prev_node = prev
                    prev.next_node = next
                    return
                self.pop_tail()
            if temp_node.next_node is not None:
                temp_node = temp_node.next_node

    @property
    def get_head(self) -> PlayerNode:
        return self._start

    @property
    def get_tail(self) -> PlayerNode:
        return self._tail

    def display(self, forward=True) -> None:
        if forward:
            print("Displaying list in order:")
            if self.is_empty:
                print("Nothing here...")
                return
            temp_node = self._start
            while temp_node is not None:
                print(temp_node.__str__())
                if temp_node.next_node is not None:
                    temp_node = temp_node.next_node
                else:
                    return

        print("Displaying list in reverse order:")
        temp_node = self._tail
        while temp_node is not None:
            print(temp_node.__str__())
            if temp_node.prev_node is not None:
                temp_node = temp_node.prev_node
            else:
                return

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}()'
