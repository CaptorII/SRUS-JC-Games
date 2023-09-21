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
                # insert left
                current_node.left = PlayerBNode(new_player)
                return
            self.insert(new_player, current_node.left)
        elif new_player.name > current_node.value.name:
            if current_node.right is None:
                # insert right
                current_node.right = PlayerBNode(new_player)
                return
            self.insert(new_player, current_node.right)
        elif new_player.name == current_node.value.name:
            # overwrite player
            current_node = PlayerBNode(new_player)
