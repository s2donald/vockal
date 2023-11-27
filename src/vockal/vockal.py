"""
The class which is designed to handle the voice translation of a given text
"""
import os

from gtts import gTTS

from vockal.utils import utils as utl

from computeraudio.utils.constants import language_code, TRANSLATEDSPEECH


class VockalMain:
    def __init__(self, audio, language):
        self.language = language
        self.lang_code = language_code[self.language]
        self.audio = audio

    def run(self):
        transcription = self.__transcribe_audio(self.audio)
        translated_text = self.__translate_text(transcription, self.lang_code)
        speak = gTTS(text=translated_text, lang=self.lang_code, slow=False)
        speak.save(TRANSLATEDSPEECH)
        self.__remove_temp_audio(self.audio)

        return

    @staticmethod
    def __translate_text(transription, lang_code):
        return utl.translate_text(transription, lang_code)

    @staticmethod
    def __transcribe_audio(audio):
        return utl.transcribe_audio(audio)

    @staticmethod
    def __remove_temp_audio(tmp_audio):
        os.remove(tmp_audio)
