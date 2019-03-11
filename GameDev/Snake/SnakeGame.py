from Snake import Snake, Direction
import random
import threading
from time import sleep
import keyboard
import os

class SnakeGame(object):
    def __init__(self):
        self.__size = [13,13]
        self.__snake = Snake(self.__getCenterCoord())
        self.__exit = False

    def start(self):
        self.__generateFruit()
        self.__showBoard()
        self.__loop()

    def __loop(self):
        input = threading.Thread(target=self.__getInput)
        input.start()
        while not self.__exit:
            os.system('cls')
            self.__snake.move()
            self.__showBoard()
            sleep(1/self.__snake.getSpeed())

    def __getInput(self):
        while True:
            if keyboard.is_pressed('up'):
                self.__snake.setDirection(Direction.UP)
            elif keyboard.is_pressed('down'):
                self.__snake.setDirection(Direction.DOWN)
            elif keyboard.is_pressed('left'):
                self.__snake.setDirection(Direction.LEFT)
            elif keyboard.is_pressed('right'):
                self.__snake.setDirection(Direction.RIGHT)
            elif keyboard.is_pressed('esc'):
                self.__exit=True
            sleep(0.01)

    def __showBoard(self):
        for x in range(0, self.__size[1]+1):
            print('=', end='=', flush=True)
        print("")
 
        for y in range(self.__size[0]):
            print('|', end='', flush=True)
            for x in range(self.__size[1]):
                if [y,x] == self.__fruit.getPosition():
                    print('*', end=' ', flush=True)
                elif [y,x] in self.__snake.getPosition():
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

    def __getCenterCoord(self):
        return [int(self.__size[0]/2), int(self.__size[1]/2)]

    def __generateFruit(self):
        coord = self.__getRandomCoord()

        while coord in self.__snake.getPosition():
            coord = self.__getRandomCoord()

        self.__fruit = fruit(coord)


class fruit(object):
    def __init__(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position
