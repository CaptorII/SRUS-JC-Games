from app.player import Player


class PlayerBST:
    def __init__(self, root_value: Player = None):
        self._root: Player | None = root_value

    @property
    def root(self) -> Player:
        return self._root

    def insert(self, new_player: Player):
        requested_name = new_player.name
        if requested_name < self.root.name:
            # insert left
            self.insert(new_player)  # ?
        elif requested_name > self.root.name:
            # insert right
            self.insert(new_player)  # ?
