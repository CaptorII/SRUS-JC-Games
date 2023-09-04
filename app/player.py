class Player:

    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name
        self._score = 0
        self._password = ''

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    def add_password(self, new_password: str):
        self._password = new_password

    def verify_password(self, password_guess: str) -> str:
        return self._password

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
