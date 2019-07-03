from time import sleep
from abc import ABC, abstractmethod
from keyboardInput import keyboardInput
import os


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
        self._continueAfterCall = True

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
            if keyboardInput.isHeldByName('down'):
                if self._selected < len(self._actions):
                    self._selected += 1
                    return True
            elif keyboardInput.isHeldByName('up'):
                if self._selected > 1:
                    self._selected -= 1
                    return True
            elif keyboardInput.isClickedByName('enter'):
                if len(self._actions) > 0:
                    self._actions[self._selected-1].call()
                return self._continueAfterCall
            elif keyboardInput.isClickedByName('esc'):
                return False
            sleep(0.001)


class selectVerticalMenu(VerticalMenu):
    def __init__(self, name):
        super().__init__(name)
        self._continueAfterCall = False

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

class Action(Controls):
    def __init__(self, name, function, param=None):
        super().__init__(name)
        self._function = function
        self._param = param

    def call(self):
        if self._param is not None:
            self._function(self._param)
        else:
            self._function()

    def setFunction(self, function):
        self._function = function

    def getFunction(self):
        return self._function

    def setParam(self, param):
        self._param = param

    def getParam(self):
        return self._param

class switchBtn(Action):
    def __init__(self, name, checkFunction, changeFunction):
        super().__init__(name, changeFunction)
        self.__checkFunction = checkFunction
    
    def __isActive(self):
        if self.__checkFunction():
            return "ON"
        else:
            return "OFF"

    def getName(self):
        return "{}: {}".format(self._name, self.__isActive())