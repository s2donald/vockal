from datetime import time

import os
from src.vockal.utils import utils as utl
from src.vockal.recorder.listener import Listener
from src.vockal.recorder.player import Player
from src.vockal.recorder.record import Recorder
import soundfile as sf

from vockal.utils.constants import SOUNDFILE


class VockalMain():
    def __init__(self):
        pass

    def run(self):
        r = Recorder(SOUNDFILE)
        p = Player(SOUNDFILE)
        l = Listener(r, p)
        print('Hold ctrl to record, Press p to playback, Press q to quit')
        l.start()  # keyboard listener is a thread so we start it here
        l.join()  # wait for the tread to terminate so the program doesn't instantly close

        transcription = self.__transcribe_audio()
        print(transcription)
        return

    @staticmethod
    def __print_sound_details(self):
        f = sf.SoundFile(SOUNDFILE)
        print('samples = {}'.format(f.frames))
        print('sample rate = {}'.format(f.samplerate))
        print('seconds = {}'.format(f.frames / f.samplerate))

    @staticmethod
    def __transcribe_audio(self):
        return utl.transcribe_audio()

    @staticmethod
    def __remove_temp_audio(self):
        os.remove(SOUNDFILE)