from __future__ import annotations


class Player:
    def __init__(self, uid: str, name: str):
        self.uid = uid
        self.name = name

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(uid={self.uid}, name={self.name})"
