from Board import Board
from Snake import Snake

test = Board()
test.generateFruit()
test.showBoard()

snake = Snake(test.getCenterCoord())
print(snake.getDirection())