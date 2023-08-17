from __future__ import annotations


class Player:

    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def get_uid(self) -> str:
        return self._uid

    @property
    def get_name(self) -> str:
        return self._name

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(uid={self._uid}, name={self._name})'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(uid={self._uid!r}, name={self._name!r})'
