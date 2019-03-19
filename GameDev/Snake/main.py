from SnakeGame import SnakeGame, Difficulty
from Menu import Menu, Action
import colorama

def displayHighScore(difficulty):
    prev = game.getDifficulty()
    game.setDifficulty(difficulty)
    game.displayTopScores()
    game.setDifficulty(prev)

colorama.init()

game = SnakeGame()

main = Menu("Main Menu")
main.addAction(Action("Start game", game.start))

options = Menu("Options")
main.addAction(options)

highScore = Menu("HighScore")
highScore.addAction(Action("EASY", displayHighScore, Difficulty.EASY))
highScore.addAction(Action("NORMAL", displayHighScore, Difficulty.NORMAL))
highScore.addAction(Action("HARD", displayHighScore, Difficulty.HARD))
main.addAction(highScore)

main.call()