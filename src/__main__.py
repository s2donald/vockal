from computeraudio.computeraudio import ComputerAudio
from computeraudio.utils.constants import INITIALSOUNDFILE
from src.vockal.vockal import VockalMain


def Vockal():
    voc = VockalMain()
    return voc


if __name__ == "__main__":
    location = ComputerAudio(INITIALSOUNDFILE).run()
    result = VockalMain(location, "Chinese (PRC)")
    result.run()
