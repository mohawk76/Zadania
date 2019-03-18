from SnakeGame import SnakeGame, move_cursor
import threading
from time import sleep
import keyboard
import colorama

colorama.init()

print("======Snake======")
print()
print("\tPlay!")
print("\tOptions")
print("\tExit")
print()
print("=================")

test = SnakeGame(15,15)
test.start()
