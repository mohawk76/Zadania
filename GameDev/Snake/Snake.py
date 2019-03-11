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

        x=position[1]
        y=position[0]

        self.__body = [SnakeBody([y,x]), SnakeBody([y,x-1]), SnakeBody([y,x-2])]


    def getDirection(self):
        return self.__direction

    def setDirection(self, direction):
        self.__direction = direction

    def getLength(self):
        return self.__length

    def getSpeed(self):
        return self.__speed

    def incLength(self):
        self.__length += 1
        self.__body.append(SnakeBody(self.__body[-1].getPosition()))

    def incSpeed(self):
        if self.__speed < 15:
            self.__speed += 1

    def getPosition(self):
        return [part.getPosition() for part in self.__body]

    def move(self):
        nextPos = self.__body[0].getPosition()
        for part in self.__body:
            #głowa
            if part == self.__body[0]:
                coords = part.getPosition()

                if self.__direction==Direction.UP:
                    coords[0]-=1
                elif self.__direction==Direction.DOWN:
                    coords[0] += 1
                elif self.__direction==Direction.LEFT:
                    coords[1] -= 1
                elif self.__direction==Direction.RIGHT:
                    coords[1] += 1
                part.setPosition(coords)
            #reszta elementów ciała
            else:
                temp = part.getPosition()
                part.setPosition(nextPos)
                nextPos = temp

class SnakeBody(object):
    def __init__(self, position):
        self.__x = position[1]
        self.__y = position[0]

    def getPosition(self):
        return [self.__y, self.__x]

    def setPosition(self, position):
        self.__x = position[1]
        self.__y = position[0]