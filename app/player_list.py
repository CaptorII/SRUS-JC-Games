from __future__ import annotations
from app.player_node import PlayerNode


class EmptyListError(Exception):
    pass


class PlayerList:
    def __init__(self):
        self._head: PlayerNode | None = None
        self._tail: PlayerNode | None = None

    def add_node_to_head(self, new_node: PlayerNode):
        if self.is_empty:  # check if adding to empty list first
            self._head = new_node
            self._tail = new_node
            return
        current_node = self._head  # if list not empty, replace current head with new node
        self._head = new_node
        self._head.next_node = current_node
        current_node.prev_node = self._head

    def add_node_to_tail(self, new_node: PlayerNode):
        if self.is_empty:
            self._head = new_node
            self._tail = new_node
            return
        current_node = self._tail
        self._tail = new_node
        self._tail.prev_node = current_node
        current_node.next_node = self._tail

    def pop_head(self):
        if self.is_empty:
            raise EmptyListError("Requested list is empty, cannot remove node")
        if self._head.next_node is None:
            self._head = None
            return
        self._head = self._head.next_node
        self._head.prev_node = None

    def pop_tail(self):
        if self.is_empty:
            raise EmptyListError("Requested list is empty, cannot remove node")
        if self._tail.prev_node is None:
            self._tail = None
            return
        self._tail = self._tail.prev_node
        self._tail.next_node = None

    def pop_key(self, key: str):
        if self.is_empty:
            raise EmptyListError("Requested list is empty, cannot remove node")
        current_node = self._head
        if current_node.key == key:  # if head or tail keys match specified keys
            self.pop_head()  # pop them first, then return
            return
        if self.tail.key == key:
            self.pop_tail()
            return
        while current_node.next_node is not None:  # search list other than head/tail
            if current_node.key == key:  # if key matches, delete by updating references, then return
                next = current_node.next_node
                prev = current_node.prev_node
                next.prev_node = prev
                prev.next_node = next
                return
            current_node = current_node.next_node  # if this node does not match, move onto next node

    @property
    def head(self) -> PlayerNode | None:
        return self._head

    @head.setter
    def head(self, new_node: PlayerNode | None):
        self._head = new_node

    @property
    def tail(self) -> PlayerNode | None:
        return self._tail

    @tail.setter
    def tail(self, new_node: PlayerNode | None):
        self._tail = new_node

    @property
    def is_empty(self) -> bool:
        return self._head is None

    def display(self, forward=True):
        if forward:
            print("Displaying list in order:")
            if self.is_empty:
                print("Nothing here...")
                return
            current_node = self._head
            while current_node is not None:
                print(current_node.__str__())
                if current_node.next_node is not None:
                    current_node = current_node.next_node
                else:
                    return

        print("Displaying list in reverse order:")
        if self.is_empty:
            print("Nothing here...")
            return
        current_node = self._tail
        while current_node is not None:
            print(current_node.__str__())
            if current_node.prev_node is not None:
                current_node = current_node.prev_node
            else:
                return

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}()'
