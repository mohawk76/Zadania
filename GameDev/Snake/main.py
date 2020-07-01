import colorama

from keyboardInput import keyboardInput
from Menu import (Action, VerticalMenu, selectHorizontalMenu,
                  selectVerticalMenu, switchBtn)
from SnakeGame import Difficulty, SnakeGame
from SystemFunctions import getFocus
from TerminalFormat import isFullScreen, toggleFullscreen, setFontSize

colorama.init()
keyboardInput.initialize()

game = SnakeGame()

main = VerticalMenu("Main Menu")
main.addAction(Action("Start game", game.start))

multi = VerticalMenu("Multiplayer")
main.addAction(multi)

options = VerticalMenu("Options")

difficultySelect = selectHorizontalMenu("Difficulty")

difficultySelect.addAction(Action("EASY", game.setDifficulty, Difficulty.EASY))
difficultySelect.addAction(Action("NORMAL", game.setDifficulty, Difficulty.NORMAL))
difficultySelect.addAction(Action("HARD", game.setDifficulty, Difficulty.HARD))
difficultySelect.setSelectedItem(game.getDifficulty().name)

options.addAction(difficultySelect) 

soundSwitch = switchBtn("Sound", game.isSoundOn, game.toogleSound)
options.addAction(soundSwitch)

musicSwitch = switchBtn("Music", game.isMusicOn, game.toogleMusic)
options.addAction(musicSwitch)

fullScreenSwitch = switchBtn("Fullscreen", isFullScreen, toggleFullscreen)
options.addAction(fullScreenSwitch)

main.addAction(options)

highScore = VerticalMenu("HighScore")
highScore.addAction(Action("EASY", game.displayHighScore, Difficulty.EASY))
highScore.addAction(Action("NORMAL", game.displayHighScore, Difficulty.NORMAL))
highScore.addAction(Action("HARD", game.displayHighScore, Difficulty.HARD))
main.addAction(highScore)

getFocus()

main.call()

keyboardInput.unhook()
