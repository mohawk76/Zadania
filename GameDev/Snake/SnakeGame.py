from Board import Board
from Snake import Snake, Direction
import threading
from time import sleep
import keyboard
import os

class SnakeGame(object):
    def __init__(self):
        self.__board = Board(13,13)
        self.__snake = Snake(self.__board.getCenterCoord())
        self.__exit = False

    def start(self):
        self.__board.generateFruit()
        self.__board.setSnakePos(self.__snake.getPosition())
        self.__board. showBoard()
        self.__loop()

    def __loop(self):
        input = threading.Thread(target=self.__getInput)
        input.start()
        while not self.__exit:
            os.system('cls')
            self.__snake.move()
            self.__board.setSnakePos(self.__snake.getPosition())
            self.__board.showBoard()
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