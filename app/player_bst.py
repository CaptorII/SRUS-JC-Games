from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self, root_player: Player = None):
        self._root: PlayerBNode | None = PlayerBNode(root_player)
        self.node_list: list[PlayerBNode] = [self._root]

    @property
    def root(self) -> PlayerBNode:
        return self._root

    def insert(self, new_player: Player, current_node: PlayerBNode = None):
        new_node = PlayerBNode(new_player)
        if current_node is None:
            current_node = self.root
        if new_player.name < current_node.value.name:
            if current_node.left is None:
                current_node.left = new_node  # insert left
                self.node_list.append(new_node)
                return
            self.insert(new_player, current_node.left)
        elif new_player.name > current_node.value.name:
            if current_node.right is None:
                current_node.right = new_node  # insert right
                self.node_list.append(new_node)
                return
            self.insert(new_player, current_node.right)
        elif new_player.name == current_node.value.name:
            current_node = new_node  # overwrite player
            self.node_list.append(new_node)

    def search(self, name: str, current_node: PlayerBNode = None) -> PlayerBNode | None:
        if current_node is None:
            current_node = self.root
        if name == current_node.value.name:
            return current_node
        if name < current_node.value.name and current_node.left is not None:
            return self.search(name, current_node.left)
        if name > current_node.value.name and current_node.right is not None:
            return self.search(name, current_node.right)
        return None

    def balance_tree(self):
        for node in self.node_list:  # reset node connections
            node.left = None
            node.right = None
        self.node_list.sort()
        list_length = len(self.node_list)
        median_index = int(list_length / 2)
        median_node = self.node_list[median_index]
        self._root = median_node
        low_index = median_index - 1
        if low_index > 0:  # if there is more than one object left of the median
            median_node.left = self.loop_through(self.node_list[0:low_index])
        else:
            median_node.left = self.node_list[low_index]
        high_index = median_index + 1
        if high_index < list_length - 1:  # if there is more than one object right of the median
            median_node.right = self.loop_through(self.node_list[high_index:list_length])
        elif high_index == list_length - 1:
            median_node.right = self.node_list[high_index]

    def loop_through(self, current_list: list[PlayerBNode]) -> PlayerBNode:
        list_length = len(current_list)
        median_index = int(list_length / 2)
        median_node = current_list[median_index]
        low_index = median_index - 1
        if low_index > 0:  # if there is more than one object left of the median
            median_node = self.loop_through(current_list[0:low_index])
        else:
            return current_list[0]
        high_index = median_index + 1
        if high_index < list_length - 1:  # if there is more than one object right of the median
            median_node = self.loop_through(current_list[high_index:list_length])
        else:
            return current_list[0]
