from Board import Board
from Snake import Snake, Direction
from time import sleep
import os

class SnakeGame(object):
    def __init__(self):
        self.__board = Board(13,13)
        self.__snake = Snake(self.__board.getCenterCoord())

    def start(self):
        self.__board.generateFruit()
        self.__board.setSnakePos(self.__snake.getPosition())
        self.__board. showBoard()
        self.__loop()

    def __loop(self):
        while True:
            os.system('cls')
            self.__snake.move()
            self.__board.setSnakePos(self.__snake.getPosition())
            self.__board.showBoard()
            sleep(1/self.__snake.getSpeed())
