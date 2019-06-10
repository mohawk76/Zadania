from time import sleep
from abc import ABC, abstractmethod
import os
import keyboard


class Controls(ABC):
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    @abstractmethod
    def call(self):
        pass


class Menu(Controls):
    def __init__(self, name):
        super().__init__(name)
        self._actions = []
        self._selected = 1

    def addAction(self, action):
        self._actions.append(action)

    def delAction(self, name):
        for action in self._actions:
            if action.getName() is name:
                self._actions.remove(action)

    def call(self):
        os.system("cls")

        self.show()
        while self._getInput():
            self.show()
            sleep(0.2)

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def _getInput(self):
        pass


class VerticalMenu(Menu):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        os.system("cls")
        menu = "======"+self._name+"======\n\n"
        index = 1

        for action in self._actions:
            menu += action.getName()
            if index == self._selected:
                menu += " <\n"
            else:
                menu += "\n"
            index += 1

        menu += "\n============"
        print(menu)

    def call(self):
        self._selected = 1
        super().call()

    def _getInput(self):
        while True:
            if keyboard.is_pressed('down'):
                if self._selected < len(self._actions):
                    self._selected += 1
                    return True
            elif keyboard.is_pressed('up'):
                if self._selected > 1:
                    self._selected -= 1
                    return True
            elif keyboard.is_pressed('enter'):
                if len(self._actions) > 0:
                    self._actions[self._selected-1].call()
                return True
            elif keyboard.is_pressed('esc'):
                return False
            sleep(0.001)


class selectVerticalMenu(VerticalMenu):
    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        if(self._actions):
            return self._name + ": " + self._actions[self._selected-1].getName()
        else:
            return self._name

    def setSelectedItem(self, actionName):
        index = 1
        for item in self._actions:
            if item.getName() == actionName:
                self._selected = index
            index += 1

    def getSelectedItem(self):
        return self._actions[self._selected-1]

    #TODO Wykombinować jak wykorzystać kod metody z klasy rodzica, by nie powielać kodu
    def _getInput(self):
        while True:
            if keyboard.is_pressed('down'):
                if self._selected < len(self._actions):
                    self._selected += 1
                    return True
            elif keyboard.is_pressed('up'):
                if self._selected > 1:
                    self._selected -= 1
                    return True
            elif keyboard.is_pressed('enter'):
                if len(self._actions) > 0:
                    self._actions[self._selected-1].call()
                return False
            elif keyboard.is_pressed('esc'):
                return False
            sleep(0.001)


class Action(Controls):
    def __init__(self, name, function, param=None):
        super().__init__(name)
        self.__function = function
        self.__param = param

    def call(self):
        if self.__param is not None:
            self.__function(self.__param)
        else:
            self.__function()

    def setFunction(self, function):
        self.__function = function

    def getFunction(self):
        return self.__function

    def setParam(self, param):
        self.__param = param

    def getParam(self):
        return self.__param
