from enum import Enum

class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3
    Custom = 4

    def __int__(self):
        return self.value