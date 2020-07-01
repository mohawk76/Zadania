from Direction import Direction
from gameObject import gameObject


class Snake(object):
    def __init__(self, position):
        self.__length = 3
        self.__speed = 3
        self.__direction = Direction.RIGHT
        self.__directionChanged = False
        x = position[1]
        y = position[0]

        self.__body = [gameObject([y, x]), gameObject(
            [y, x-1]), gameObject([y, x-2])]

    def getDirection(self):
        return self.__direction

    def setDirection(self, direction):
        if self.__directionChanged is False:
            self.__direction = direction
            self.__directionChanged = True

    def getLength(self):
        return self.__length

    def getSpeed(self):
        return self.__speed

    def incLength(self):
        self.__length += 1
        self.__body.append(gameObject(self.__body[-1].getPosition()))

    def incSpeed(self):
        if self.__speed < 15:
            self.__speed += 1

    def getPosition(self):
        return [part.getPosition() for part in self.__body]

    def move(self):
        self.__directionChanged = False
        nextPos = self.__body[0].getPosition()
        for part in self.__body:
            # głowa
            if part == self.__body[0]:
                coords = part.getPosition()

                if self.__direction == Direction.UP:
                    coords[0] -= 1
                elif self.__direction == Direction.DOWN:
                    coords[0] += 1
                elif self.__direction == Direction.LEFT:
                    coords[1] -= 1
                elif self.__direction == Direction.RIGHT:
                    coords[1] += 1
                part.setPosition(coords)
            # reszta elementów ciała
            else:
                temp = part.getPosition()
                part.setPosition(nextPos)
                nextPos = temp
