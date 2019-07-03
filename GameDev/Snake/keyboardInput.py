import keyboard
import sys
import os

class keyState:
    def __init__(self):
        self.bPressed = False
        self.bReleased = False
        self.bHeld = False
        self.lastState = None

class keyboardInput:

    @staticmethod
    def initialize():
        keyboardInput.__keyList = []
        for x in range(542):
            keyboardInput.__keyList.append(keyState())
        keyboard.hook(keyboardInput.__hookInput)

    @staticmethod
    def __hasFocus():
        if sys.platform in ['linux', 'linux2']:
            import wnck
            screen = wnck.screen_get_default()
            screen.force_update()
            window = screen.get_active_window()

            if window is not None:
                return window.get_pid() == os.getppid()

            return False            
        elif sys.platform in ['Windows', 'win32', 'cygwin']:
            import win32gui
            import win32process
            return win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1] == os.getppid()
        else:
            return True

    @staticmethod
    def __hookInput(keyEvent : keyboard.KeyboardEvent):
        if not keyboardInput.__hasFocus():
            return
        
        keyboardInput.__keyList[keyEvent.scan_code].bPressed = False
        keyboardInput.__keyList[keyEvent.scan_code].bReleased = False

        if keyboardInput.__keyList[keyEvent.scan_code].lastState is not keyEvent.event_type:
            if keyEvent.event_type is keyboard.KEY_DOWN:
                keyboardInput.__keyList[keyEvent.scan_code].bPressed = not keyboardInput.__keyList[keyEvent.scan_code].bHeld
                keyboardInput.__keyList[keyEvent.scan_code].bHeld = True
            else:
                keyboardInput.__keyList[keyEvent.scan_code].bReleased = True
                keyboardInput.__keyList[keyEvent.scan_code].bHeld = False
        keyboardInput.__keyList[keyEvent.scan_code].lastState = keyEvent.event_type

    @staticmethod
    def isHeldByName(name:str) -> bool:
        return keyboardInput.isHeld(keyboard.key_to_scan_codes(name)[0])

    @staticmethod
    def isHeld(scan_code:int) -> bool:
        return keyboardInput.__keyList[scan_code].bHeld

    @staticmethod
    def isReleasedByName(name:str) -> bool:
        return keyboardInput.isReleased(keyboard.key_to_scan_codes(name)[0])

    @staticmethod
    def isReleased(scan_code:int) -> bool:
        return keyboardInput.__keyList[scan_code].bReleased

    @staticmethod
    def isPressedByName(name:str) -> bool:
        return keyboardInput.isPressed(keyboard.key_to_scan_codes(name)[0])

    @staticmethod
    def isPressed(scan_code:int) -> bool:
        return keyboardInput.__keyList[scan_code].bPressed

    @staticmethod
    def isClickedByName(name:str) -> bool:
        return keyboardInput.isClicked(keyboard.key_to_scan_codes(name)[0])

    @staticmethod
    def isClicked(scan_code:int) -> bool:
        if keyboardInput.__keyList[scan_code].bPressed:
            keyboardInput.__keyList[scan_code].bPressed = False
            return True
        return False

    @staticmethod
    def unhook():
        keyboard.unhook_all()