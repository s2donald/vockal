"""This class is meant to handle the Recording, Listening and Output of the audio file"""
from computeraudio.recorder.listener import Listener
from computeraudio.recorder.player import Player
from computeraudio.recorder.record import Recorder


class ComputerAudio():
    def __init__(self, location):
        self.location = location
        self.r = Recorder(self.location)
        self.p = Player(self.location)
        self.l = Listener(self.r, self.p)

    def run(self):
        print("Hold ctrl to record, Press p to playback, Press q to quit")
        self.l.start()  # keyboard listener is a thread so we start it here
        self.l.join()  # wait for the tread to terminate so the program doesn't instantly close
        return self.location
