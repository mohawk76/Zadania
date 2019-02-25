import random

class Board(object):
    def __init__(self):
        self.__size = [13,13]
        self.__matrix = [[' ' for x in range(self.__size[0])] for y in range(self.__size[1])]
        self.__fruit = "*"

    def showBoard(self):
        for x in range(0, self.__size[1]+1):
            print('=', end='=', flush=True)
        print("")

        for row in self.__matrix:
            print('|', end='', flush=True)
            for val in row:
                print(val, end=' ', flush=True)
            print('|', end='', flush=True)
            print("")

        for x in range(0, self.__size[1] + 1):
            print('=', end='=', flush=True)
        print("")

    def __getRandomCoord(self):
        return [random.randint(0,self.__size[0]-1), random.randint(0,self.__size[1]-1)]

    def getCenterCoord(self):
        return [self.__size[0]/2, self.__size[1]/2]

    def generateFruit(self):
        cord = self.__getRandomCoord()
        self.__matrix[cord[0]][cord[1]] =self.__fruit

    def draw(self, x, y, char):
        if x<0 or y<0:
            raise Exception("IndexOutOfBoundsException")
        elif x>self.__size[1] or y>self.__size[0]:
            raise Exception("IndexOutOfBoundsException")

        self.__matrix[y][x] = char
