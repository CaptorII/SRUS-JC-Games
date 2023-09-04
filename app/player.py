from argon2 import PasswordHasher
ph = PasswordHasher()


class Player:
    def __init__(self, uid: str, name: str):
        self._uid: str = uid
        self._name: str = name
        self._hashed_password: str | None = None
        self._score: int = 0

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    def add_password(self, new_password: str):
        self._hashed_password = ph.hash(new_password)

    def verify_password(self, password_guess: str = None) -> bool:
        if password_guess is None:
            raise TypeError("No password provided")
        if self._hashed_password is None:
            raise TypeError("No password on account")
        return ph.verify(self._hashed_password, password_guess)

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int):
        self._score = value

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(uid= {self._uid}, name= {self._name})'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(uid={self._uid!r}, name={self._name!r})'

    def __eq__(self, other):
        return self._score == other.score

    def __ge__(self, other):
        return self._score >= other.score

    def __le__(self, other):
        return self._score <= other.score

    def __lt__(self, other):
        return self._score < other.score

    def __gt__(self, other):
        return self._score > other.score
