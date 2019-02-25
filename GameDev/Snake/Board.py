class Board(object):
    def __init__(self):
        self.__matrix = [[0 for x in range(12)] for y in range(12)]

    def showBoard(self):
        for row in self.__matrix:
            for val in row:
                print(val, end=' ', flush=True)
            print("")
