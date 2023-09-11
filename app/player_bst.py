class PlayerBST:
    def __init__(self, root_value: int = None):
        self._root = root_value

    @property
    def root(self) -> int:
        return self._root
    