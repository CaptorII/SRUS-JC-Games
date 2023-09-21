from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self, root_player: Player = None):
        self._root: PlayerBNode | None = PlayerBNode(root_player)

    @property
    def root(self) -> PlayerBNode:
        return self._root

    def insert(self, new_player: Player, current_node: PlayerBNode = None):
        if current_node is None:
            current_node = self.root
        if new_player.name < current_node.value.name:
            if current_node.left is None:
                current_node.left = PlayerBNode(new_player)  # insert left
                return
            self.insert(new_player, current_node.left)
        elif new_player.name > current_node.value.name:
            if current_node.right is None:
                current_node.right = PlayerBNode(new_player)  # insert right
                return
            self.insert(new_player, current_node.right)
        elif new_player.name == current_node.value.name:
            current_node = PlayerBNode(new_player)  # overwrite player

    def search(self, name: str, current_node: PlayerBNode = None) -> PlayerBNode | None:
        if current_node is None:
            current_node = self.root
        if name == current_node.value.name:
            return current_node
        if name < current_node.value.name and current_node.left is not None:
            current_node = self.search(name, current_node.left)
            return current_node
        if name > current_node.value.name and current_node.right is not None:
            current_node = self.search(name, current_node.right)
            return current_node
        return None
