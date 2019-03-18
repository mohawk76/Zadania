from Snake import Snake, Direction
from time import sleep
from enum import Enum
import random
import threading
import os
import json
import keyboard

def move_cursor(x, y):
    print("\x1b[{};{}H".format(y + 1, x + 1), end='')

def getScoresKey(e):
    return e["Score"]

class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3
    
    def __int__(self):
        return self.value

class SnakeGame:
    def __init__(self, x, y):
        self.__size = [y,x]
        self.__snake = Snake(self.__getCenterCoord())
        self.__fruit = fruit([-1,-1])
        self.__exit = False
        self.__score = 0
        self.__difficulty = Difficulty.NORMAL
        self.__topScore = []

    def start(self):
        os.system("cls")
        self.__loadScores()
        self.__generateFruit()
        self.__showBoard()
        self.__loop()

    def __loop(self):
        inputThread = threading.Thread(target=self.__getInput)
        inputThread.start()
        while not self.__exit:
            self.__snake.move()
            self.__detectCollision()
            self.__showBoard()
            sleep(1/self.__snake.getSpeed())

        self.__gameOver()
        
        playerName = ""
        if self.__checkQualifyTopScore():
            playerName = input("PlayerName: ")
            self.__updateScores(playerName)
            self.__saveScores()
        
        self.__displayTopScores()
            

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
        move_cursor(0,0)

        board = "Score: {}\n".format(self.__score)
        for x in range(0, self.__size[1]+1):
            if x==0:
                board += "+="
            elif x==self.__size[1]:
                board += "=+"
            else:
                board += "=="
        board += "\n"
 
        for y in range(self.__size[0]):
            board += "|"
            for x in range(self.__size[1]):
                if [y,x] == self.__fruit.getPosition():
                    board += "* "
                elif [y,x] in self.__snake.getPosition():
                    board += "o "
                else:
                    board += "  "
            board += "|\n"

        for x in range(0, self.__size[1] + 1):
            if x==0:
                board += "+="
            elif x==self.__size[1]:
                board += "=+"
            else:
                board += "=="
        board += "\n"
        print(board)

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

    def __gameOver(self):
        os.system("cls")
        print("======GAME OVER!======\n\n")
        print("   Difficulty: "+self.__difficulty.name)
        print("   Score: "+str(self.__score)+"\n\n")
        os.system("pause")
        os.system("cls")

    def __loadScores(self):
        if os.path.isfile("data/score"+self.__difficulty.name+".json"):
            with open("data/score"+self.__difficulty.name+".json", "r") as jsonScores:
                self.__topScore = json.load(jsonScores)

    def __saveScores(self):
         with open("data/score"+self.__difficulty.name+".json", "w") as scoresFile:
             scoresFile.write(json.dumps(self.__topScore))

    def __checkQualifyTopScore(self):
        if self.__score is 0:
            return False

        if(len(self.__topScore)<10):
            return True
        
        for score in self.__topScore:
            if score["Score"]<=self.__score:
                return True
        return False

    def __updateScores(self, playerName):
        self.__topScore.append({"Name": playerName, "Score": self.__score})
        self.__topScore.sort(key=getScoresKey, reverse=True)

        while len(self.__topScore)>10:
            self.__topScore.pop()

    def __displayTopScores(self):
        os.system("cls")
        i=1

        print("======"+self.__difficulty.name+" Top 10======\n")
        for score in self.__topScore:
            print(str(i)+". " + score["Name"] + "    " + str(score["Score"]))
            i+=1
        print()
        os.system("pause")


class fruit(object):
    def __init__(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position
