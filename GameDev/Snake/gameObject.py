class gameObject(object):
    def __init__(self, position):
        self.setPosition(position)

    def getPosition(self):
        return [self.__y, self.__x]

    def setPosition(self, position):
        self.__y, self.__x = position
