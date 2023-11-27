import speech_recognition as sr
from googletrans import Translator as Trans

def transcribe_audio(audio):
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio = r.record(source)  # read the entire audio file
        try:
            transcription = r.recognize_google(audio)
        except sr.exceptions.UnknownValueError:
            print('We couldn\'t hear you properly')
            transcription = ''
    return transcription

def translate_text(text, code):
    translator1 = Trans()
    text_to_translate_1 = translator1.translate(text, dest=code)
    text1 = text_to_translate_1.text
    return text1
