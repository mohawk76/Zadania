class gameObject(object):
    def __init__(self, position):
        self.__x = position[1]
        self.__y = position[0]

    def getPosition(self):
        return [self.__y, self.__x]

    def setPosition(self, position):
        self.__x = position[1]
        self.__y = position[0]