import random

class Board(object):
    def __init__(self, height, width):
        self.__size = [height, width]
        self.__matrix = [[' ' for x in range(self.__size[0])] for y in range(self.__size[1])]
        self.__snakeCoords = []

    def showBoard(self):
        for x in range(0, self.__size[1]+1):
            print('=', end='=', flush=True)
        print("")
        x=0
        y=0
        for row in self.__matrix:
            print('|', end='', flush=True)
            for val in row:
                if [y,x] == self.__fruit.getPosition():
                    print('*', end=' ', flush=True)
                elif [y,x] in self.__snakeCoords:
                    print('o', end=' ', flush=True)
                else:
                    print(' ', end=' ', flush=True)
                x+=1
            print('|', end='', flush=True)
            print("")
            y+=1
            x=0

        for x in range(0, self.__size[1] + 1):
            print('=', end='=', flush=True)
        print("")

    def __getRandomCoord(self):
        return [random.randint(0,self.__size[0]-1), random.randint(0,self.__size[1]-1)]

    def getCenterCoord(self):
        return [int(self.__size[0]/2), int(self.__size[1]/2)]

    def generateFruit(self):
        coord = self.__getRandomCoord()

        while self.__matrix[coord[0]][coord[1]]=='o':
            coord = self.__getRandomCoord()

        self.__fruit = fruit(coord)

    def setSnakePos(self, snakeCoords):
        self.__snakeCoords = snakeCoords

class fruit(object):
    def __init__(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position
