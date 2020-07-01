import io
from os import listdir
from os.path import isfile, join

from pyglet import media


class AudioManager:
    def __init__(self):
        self.__sounds = []
        
    audioTypes = ["mp3", "wav", "ogg", "flac"]

    @staticmethod
    def isAudioFile(file):
        for filetype in AudioManager.audioTypes:
            if(filetype in file):
                return True
        return False

    def loadSoundFromDirectory(self, path):
        for f in listdir(path):
            if isfile(join(path, f)) and AudioManager.isAudioFile(f):
                self.loadSound(f.split('.')[0], join(path, f))
    
    def loadSound(self, name, path):
        if name not in self.__sounds:
            self.__sounds.append(Sound(name, path))

    def playSound(self, name):
        try:
            index = [sound.name for sound in self.__sounds].index(name)
        except:
            return
        self.__sounds[index].playSound()

    def stopSound(self, name):
        try:
            index = [sound.name for sound in self.__sounds].index(name)
        except:
            return
        self.__sounds[index].stopSound()

    def displaySounds(self):
        for sound in self.__sounds:
            print(sound.name)
        input()

    def setVolume(self, name, volume):
        try:
            index = [sound.name for sound in self.__sounds].index(name)
        except:
            return
        self.__sounds[index].setVolume(volume)

    def toggleRepeat(self, name):
        try:
            index = [sound.name for sound in self.__sounds].index(name)
        except:
            return
        self.__sounds[index].toggleRepeat()


class Sound:
    def __init__(self, name, path):
        self.name = name
        self.__error = False
        try:
            snd = media.load(path, streaming=False)

            self.__looper = media.SourceGroup(snd.audio_format, None)
            self.__looper.loop = False
            self.__looper.queue(snd)

            self.__sound = media.Player()
            self.__sound.queue(self.__looper)
        except:
           self.__error = True


    def playSound(self):
        if self.__error:
           return
        self.__sound.seek(0)
        self.__sound.play()

    def stopSound(self):
        if self.__error:
           return
        self.__sound.pause()

    def __eq__(self, other): 
        if not isinstance(other, str):
            return NotImplemented
        
        return self.name == other
    
    def setVolume(self, volume):
        if self.__error:
           return
        self.__sound.volume = volume

    def toggleRepeat(self):
        if self.__error:
           return
        self.__looper.loop = not self.__looper.loop
