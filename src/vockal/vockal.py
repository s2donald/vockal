from datetime import time

import os
import speech_recognition as sr
from src.vockal.utils import utils as utl
from src.vockal.recorder.listener import Listener
from src.vockal.recorder.player import Player
from src.vockal.recorder.record import Recorder
import soundfile as sf


class VockalMain():
    def __init__(self):
        pass

    def run(self):
        r = Recorder("mic.wav")
        p = Player("mic.wav")
        l = Listener(r, p)
        print('Hold ctrl to record, Press p to playback, Press q to quit')
        l.start()  # keyboard listener is a thread so we start it here
        l.join()  # wait for the tread to terminate so the program doesn't instantly close
        # f = sf.SoundFile('mic.wav')
        # print('samples = {}'.format(f.frames))
        # print('sample rate = {}'.format(f.samplerate))
        # print('seconds = {}'.format(f.frames / f.samplerate))
        r = sr.Recognizer()
        with sr.AudioFile('mic.wav') as source:
            audio = r.record(source)  # read the entire audio file
            print("Transcription: " + r.recognize_google(audio))
        os.remove("mic.wav")
        return

    def __record_audio(self, duration, fs, channels):
        return utl.record_audio(duration, fs, channels)

    def __transcribe_audio(self, recorded_audio, fs):
        return utl.transcribe_audio(recorded_audio, fs)