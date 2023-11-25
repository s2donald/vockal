import speech_recognition as sr
from vockal.utils.constants import SOUNDFILE


def transcribe_audio():
    r = sr.Recognizer()
    with sr.AudioFile(SOUNDFILE) as source:
        audio = r.record(source)  # read the entire audio file
        transcription = r.recognize_google(audio)
    return transcription
