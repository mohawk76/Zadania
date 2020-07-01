import os
import sys


def isWindows():
    return sys.platform in ['Windows', 'win32', 'cygwin']

def isLinux():
    return sys.platform in ['linux', 'linux2']

if isLinux():
    import wnck
elif isWindows():
    import win32gui
    import win32console
    import win32process

def hasFocus():
    if isLinux():
        screen = wnck.screen_get_default()
        screen.force_update()
        window = screen.get_active_window()

        if window is not None:
            return window.get_pid() == os.getppid()
        return False   
    elif isWindows():   
        return win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1] == os.getppid()
    else:
        return True

def getFocus():
    consoleWindow=win32console.GetConsoleWindow()
    if consoleWindow is not None:
        win32gui.SetForegroundWindow(consoleWindow)
