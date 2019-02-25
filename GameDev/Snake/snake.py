from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Snake(object):
    def __init__(self, position):
        self.__length = 3
        self.__speed = 1
        self.__direction = Direction.RIGHT
        self.__position = position

    def getDirection(self):
        return self.__direction

    def getLength(self):
        return self.__length

    def incLength(self):
        self.__length += 1

    def incSpeed(self):
        self.__speed += 1