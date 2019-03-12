from Snake import Snake, Direction
import random
import threading
from time import sleep
import keyboard
import os
from enum import Enum

class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3
    
    def __int__(self):
        return self.value

class SnakeGame(object):
    def __init__(self):
        self.__size = [13,13]
        self.__snake = Snake(self.__getCenterCoord())
        self.__fruit = fruit([-1,-1])
        self.__exit = False
        self.__score = 0
        self.__difficulty = Difficulty.NORMAL

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
            self.__detectCollision()
            self.__showBoard()
            sleep(1/self.__snake.getSpeed())

    def __getInput(self):
        while not self.__exit:
            if keyboard.is_pressed('up') and self.__snake.getDirection() != Direction.DOWN:
                self.__snake.setDirection(Direction.UP)
            elif keyboard.is_pressed('down') and self.__snake.getDirection() != Direction.UP:
                self.__snake.setDirection(Direction.DOWN)
            elif keyboard.is_pressed('left') and self.__snake.getDirection() != Direction.RIGHT:
                self.__snake.setDirection(Direction.LEFT)
            elif keyboard.is_pressed('right') and self.__snake.getDirection() != Direction.LEFT:
                self.__snake.setDirection(Direction.RIGHT)
            elif keyboard.is_pressed('esc'):
                self.__exit=True
            sleep(0.01)

    def __showBoard(self):
        print("Score: {}".format(self.__score))
        for x in range(0, self.__size[1]+1):
            if x==0:
                print('+', end='=', flush=True)
            elif x==self.__size[1]:
                print('=', end='+', flush=True)
            else:
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

        for x in range(0, self.__size[1] + 1):
            if x==0:
                print('+', end='=', flush=True)
            elif x==self.__size[1]:
                print('=', end='+', flush=True)
            else:
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

        self.__fruit.setPosition(coord)

    def __detectCollision(self):
        if self.__snake.getPosition()[0]==self.__fruit.getPosition():
            self.__score+=10*int(self.__difficulty)
            self.__snake.incLength()
            self.__generateFruit()
            if self.__difficulty is Difficulty.NORMAL and self.__snake.getSpeed() < 9:
                self.__snake.incSpeed()
        elif self.__snake.getPosition()[0] in self.__snake.getPosition()[1:]:
            self.__exit = True
        elif self.__snake.getPosition()[0][0] < 0 or self.__snake.getPosition()[0][0]>self.__size[0]-1:
            self.__exit = True
        elif self.__snake.getPosition()[0][1] < 0 or self.__snake.getPosition()[0][1]>self.__size[1]-1:
            self.__exit = True

class fruit(object):
    def __init__(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position
