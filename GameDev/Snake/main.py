from SnakeGame import SnakeGame, Difficulty
from Menu import VerticalMenu, Action, selectVerticalMenu
import colorama


colorama.init()

game = SnakeGame()

main = VerticalMenu("Main Menu")
main.addAction(Action("Start game", game.start))

multi = VerticalMenu("Multiplayer")
main.addAction(multi)


options = VerticalMenu("Options")
difficultySelect = selectVerticalMenu("Difficulty")

difficultySelect.addAction(Action("EASY", game.setDifficulty, Difficulty.EASY))
difficultySelect.addAction(Action("NORMAL", game.setDifficulty, Difficulty.NORMAL))
difficultySelect.addAction(Action("HARD", game.setDifficulty, Difficulty.HARD))
difficultySelect.setSelectedItem(game.getDifficulty().name)

options.addAction(difficultySelect)
main.addAction(options)

highScore = VerticalMenu("HighScore")
highScore.addAction(Action("EASY", game.displayHighScore, Difficulty.EASY))
highScore.addAction(Action("NORMAL", game.displayHighScore, Difficulty.NORMAL))
highScore.addAction(Action("HARD", game.displayHighScore, Difficulty.HARD))
main.addAction(highScore)

main.call()
