import os
from SystemFunctions import isLinux, isWindows

if isWindows():
    import win32console
    console = win32console.PyConsoleScreenBufferType(win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE))
    
def move_cursor(x:int, y:int):
    print("\x1b[{};{}H".format(y + 1, x + 1), end='')

def display(text:str, color):
    print(text, end="")

def resizeTerminal(rows:int, cols:int):
    if isLinux():
        print("\x1b[8;{};{}t".format(rows, cols))
    elif isWindows():
        os.system("mode con: cols={} lines={}".format(cols,rows))

def repeatNChar(size: int, char: chr)->str:
    return ""+char*size

def space(size:int=1)->str:
    return repeatNChar(size, ' ')

def setFontSize(size:int):
    if isWindows():
        global console
        
        ind, coord = console.GetCurrentConsoleFont()
        console.SetConsoleFont(ind)
        print(console.GetConsoleFontSize(ind))
        input()
    elif isLinux():
        raise NotImplementedError

def isFullScreen()->bool:
    if isWindows():
        return win32console.GetConsoleDisplayMode() == 1
    elif isLinux():
        return False
    
def toggleFullscreen():
    if isWindows():
        global console
        if not isFullScreen():
            console.SetConsoleDisplayMode(win32console.CONSOLE_FULLSCREEN_MODE, win32console.PyCOORDType(0,0))
        else:
            console.SetConsoleDisplayMode(win32console.CONSOLE_WINDOWED_MODE, win32console.PyCOORDType(0,0))
    elif isLinux():
        raise NotImplementedError
    