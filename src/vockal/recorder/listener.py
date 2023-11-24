from pynput import keyboard

from vockal.recorder.player import Player
from vockal.recorder.record import Recorder


class Listener(keyboard.Listener):
    def __init__(self, recorder: Recorder, player: Player):
        super().__init__(on_press=self.on_press, on_release=self.on_release)
        self.recorder = recorder
        self.player = player

    def on_press(self, key):
        if key is None:  # unknown event
            pass
        elif isinstance(key, keyboard.Key):  # special key event
            if key.ctrl and self.player.playing == 0:
                self.recorder.start()
        elif isinstance(key, keyboard.KeyCode):  # alphanumeric key event
            if key.char == 'q':  # press q to quit
                if self.recorder.recording:
                    self.recorder.stop()
                return False  # this is how you stop the listener thread
            if key.char == 'p' and not self.recorder.recording:
                self.player.start()

    def on_release(self, key):
        if key is None:  # unknown event
            pass
        elif isinstance(key, keyboard.Key):  # special key event
            if key.ctrl:
                self.recorder.stop()
        elif isinstance(key, keyboard.KeyCode):  # alphanumeric key event
            pass