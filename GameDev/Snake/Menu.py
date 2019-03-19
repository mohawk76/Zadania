from time import sleep
import os
import keyboard

class Menu(object):
    def __init__(self, name):
        self.__name = name
        self.__actions = []

    def addAction(self, action):
        self.__actions.append(action)

    def delAction(self, name):
        for action in self.__actions:
            if action.getName() is name:
                self.__actions.remove(action)

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def call(self):
        os.system("cls")
        self.__selected = 1
        
        self.show()
        while self.__getInput():
            self.show()
            sleep(0.1)

    def show(self):
        os.system("cls")
        menu = "======"+self.__name+"======\n\n"
        index = 1

        for action in self.__actions:
            menu += action.getName()
            if index == self.__selected:
                menu += " <\n"
            else:
                menu += "\n"
            index+=1

        menu += "============"
        print(menu)

    def __getInput(self):
        while True:
            if keyboard.is_pressed('down'):
                if self.__selected<len(self.__actions):
                    self.__selected+=1
                    return True
            elif keyboard.is_pressed('up'):
                if self.__selected>1:
                    self.__selected-=1
                    return True
            elif keyboard.is_pressed('enter'):
                if len(self.__actions)>0:
                    self.__actions[self.__selected-1].call()
                return True
            elif keyboard.is_pressed('esc'):
                return False
            sleep(0.001)

class Action(object):
    def __init__(self, name, function, param = None):
        self.__name = name
        self.__function = function
        self.__param = param

    def call(self):
        if self.__param is not None:
            self.__function(self.__param)
        else:
            self.__function()

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setFunction(self, function):
        self.__function = function
    
    def getFunction(self):
        return self.__function

    def setParam(self, param):
        self.__param = param
    
    def getParam(self):
        return self.__param