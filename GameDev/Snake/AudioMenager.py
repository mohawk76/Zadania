from pydub import AudioSegment
from pydub.playback import play
import io

class AudioMenager:
    def __init__(self):
        self.__audioFiles = []
        self.__cachedSounds = []
        self
