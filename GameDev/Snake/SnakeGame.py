from Snake import Snake
from Direction import Direction
from keyboardInput import keyboardInput
from AudioMenager import AudioMenager
from TerminalFormat import move_cursor
from gameObject import gameObject
from Difficulty import Difficulty
from time import sleep
from colorama import Fore
from keyboard import key_to_scan_codes
import random
import threading
import os
import json

def getScoresKey(e):
    return e["Score"]

class SnakeGame:
    def __init__(self):
        self.__size = [12, 12]
        self.__fruitsQuantity = 0
        self.__difficulty = Difficulty.NORMAL
        self.__topScore = []
        self.__loadScores()

        self.__audioMenager = AudioMenager()
        self.__audioMenager.loadSoundFromDirectory('sounds')
        self.__audioMenager.setVolume("gameMusic", 0.0001)
        self.__audioMenager.toggleRepeat("gameMusic")
        
        #self.__audioMenager.displaySounds()

        self.__soundON = True
        self.__musicON = True

        if self.__musicON:
            self.__audioMenager.playSound('gameMusic')

    def getBoardSize(self):
        return self.__size

    def setBoardSize(self, width, heigth):
        self.__size = [heigth, width]

    def getDifficulty(self):
        return self.__difficulty

    def setDifficulty(self, difficulty):
        self.__difficulty = difficulty
        self.__loadScores()

    def isSoundOn(self):
        return self.__soundON
    
    def toogleSound(self):
        self.__soundON = not self.__soundON

    def isMusicOn(self):
        return self.__musicON
    
    def toogleMusic(self):
        self.__musicON = not self.__musicON
        if self.__musicON:
            self.__audioMenager.playSound('gameMusic')
        else:
            self.__audioMenager.stopSound('gameMusic')


    def start(self):
        self.__snake = Snake(self.__getCenterCoord())
        self.__fruit = gameObject([-1, -1])
        self.__exit = False
        self.__score = 0

        if self.__difficulty == Difficulty.EASY:
            self.setBoardSize(10,10)
        elif self.__difficulty == Difficulty.NORMAL:
            self.setBoardSize(20,20)
        elif self.__difficulty == Difficulty.HARD:
            self.setBoardSize(20,20)

        os.system("cls")

        self.__generateFruit()
        self.__showBoard()
        self.__gameLoop()

    def __gameLoop(self):
        inputThread = threading.Thread(target=self.__getInput)
        inputThread.start()
        #self.__getInput()
        while not self.__exit and not self.__isWin():
            self.__snake.move()
            self.__detectCollision()
            self.__showBoard()
            sleep(1/self.__snake.getSpeed())

        if self.__soundON:
            self.__audioMenager.playSound('dead')
        
        self.__dieAnimation()
        self.__gameOver()

        playerName = ""
        if self.__checkQualifyTopScore():
            playerName = input("PlayerName: ")
            self.__updateScores(playerName)
            self.__saveScores()

        self.__displayTopScores()

        self.__audioMenager.stopSound('dead')

    def __getInput(self):
        up = key_to_scan_codes('up')[0]
        down = key_to_scan_codes('down')[0]
        left = key_to_scan_codes('left')[0]
        right = key_to_scan_codes('right')[0]
        esc = key_to_scan_codes('esc')[0]

        while not self.__exit:
            if keyboardInput.isPressed(up) and self.__snake.getDirection() != Direction.DOWN:
                self.__snake.setDirection(Direction.UP)
            elif keyboardInput.isPressed(down) and self.__snake.getDirection() != Direction.UP:
                self.__snake.setDirection(Direction.DOWN)
            elif keyboardInput.isPressed(left) and self.__snake.getDirection() != Direction.RIGHT:
                self.__snake.setDirection(Direction.LEFT)
            elif keyboardInput.isPressed(right) and self.__snake.getDirection() != Direction.LEFT:
                self.__snake.setDirection(Direction.RIGHT)
            elif keyboardInput.isClicked(esc):
                self.__exit = True
            sleep(0.0001)

    def __showBoard(self):
        move_cursor(0, 0)

        board = "Score: {}\n".format(self.__score)
        for x in range(0, self.__size[1]+1):
            if x == 0:
                board += "+="
            elif x == self.__size[1]:
                board += "==+"
            else:
                board += "=="
        board += "\n"

        for y in range(self.__size[0]):
            board += "| "
            for x in range(self.__size[1]):
                if [y, x] == self.__fruit.getPosition():
                    board += Fore.YELLOW+"* "+Fore.WHITE
                elif [y, x] in self.__snake.getPosition():
                    board += Fore.GREEN + "o "+Fore.WHITE
                else:
                    board += "  "
            board += "|\n"

        for x in range(0, self.__size[1] + 1):
            if x == 0:
                board += "+="
            elif x == self.__size[1]:
                board += "==+"
            else:
                board += "=="
        board += "\n"
        print(board)

    def __dieAnimation(self):
        y,x = self.__snake.getPosition()[0]
        x *= 2
        x+=2
        y+=2
        move_cursor(x,y)
        print(Fore.RED+"#"+Fore.WHITE, end="")
        sleep(2)


    def __getRandomCoord(self):
        return [random.randint(0, self.__size[0]-1), random.randint(0, self.__size[1]-1)]

    def __getCenterCoord(self):
        return [int(self.__size[0]/2), int(self.__size[1]/2)]

    def __generateFruit(self):
        coord = self.__getRandomCoord()

        while coord in self.__snake.getPosition():
            coord = self.__getRandomCoord()

        self.__fruit.setPosition(coord)

    def __detectCollision(self):
        if self.__snake.getPosition()[0] == self.__fruit.getPosition():
           self.__eatFruit()
        elif self.__snake.getPosition()[0] in self.__snake.getPosition()[1:]:
            self.__exit = True
        elif self.__snake.getPosition()[0][0] < 0 or self.__snake.getPosition()[0][0] > self.__size[0]-1:
            self.__exit = True
        elif self.__snake.getPosition()[0][1] < 0 or self.__snake.getPosition()[0][1] > self.__size[1]-1:
            self.__exit = True

    def __eatFruit(self):
        if self.__soundON:
            self.__audioMenager.playSound('coin')

        self.__score += 10*int(self.__difficulty)
        self.__snake.incLength()
        self.__generateFruit()
        if self.__difficulty is Difficulty.NORMAL and self.__snake.getSpeed() < 9:
            self.__snake.incSpeed()

    def __gameOver(self):
        os.system("cls")
        print(Fore.RED+"======GAME OVER!======\n\n"+Fore.WHITE)
        print("   Difficulty: "+self.__difficulty.name)
        print("   Score: "+str(self.__score)+"\n\n")
        os.system("pause")
        os.system("cls")

    def __isWin(self):
        return self.__snake.getLength() == (self.__size[0]*self.__size[1])

    def __loadScores(self):
        if os.path.isfile("data/score"+self.__difficulty.name+".json"):
            with open("data/score"+self.__difficulty.name+".json", "r") as jsonScores:
                self.__topScore = json.load(jsonScores)
        else:
            self.__topScore = []

    def __saveScores(self):
        with open("data/score"+self.__difficulty.name+".json", "w") as scoresFile:
            scoresFile.write(json.dumps(self.__topScore))

    def __checkQualifyTopScore(self):
        if self.__score is 0:
            return False

        if(len(self.__topScore) < 10):
            return True

        for score in self.__topScore:
            if (score["Score"] <= self.__score) and (score is not self.__topScore[-1]):
                return True
        return False

    def __updateScores(self, playerName):
        self.__topScore.append({"Name": playerName, "Score": self.__score})
        self.__topScore.sort(key=getScoresKey, reverse=True)

        while len(self.__topScore) > 10:
            self.__topScore.pop()

    def __displayTopScores(self):
        os.system("cls")
        i = 1

        print(Fore.YELLOW+"======"+self.__difficulty.name +
              " Top 10======\n"+Fore.WHITE)
        for score in self.__topScore:
            print(str(i)+". " + score["Name"] + "    " + str(score["Score"]))
            i += 1
        print()
        os.system("pause")

    def displayHighScore(self, difficulty):
        prev = self.getDifficulty()
        self.setDifficulty(difficulty)
        self.__displayTopScores()
        self.setDifficulty(prev)
