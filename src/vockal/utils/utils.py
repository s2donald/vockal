import sounddevice as sd
import tempfile
import soundfile as sf
import openai
import os


def record_audio(duration, fs, channels):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    return recording

def transcribe_audio(recording, fs):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        sf.write(temp_audio.name, recording, fs)
        temp_audio.close()
        with open(temp_audio.name, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        os.remove(temp_audio.name)
    return transcript["text"].strip()

def play_generated_audio(text, voice="", model=""):
    # audio = generate(text=text, voice=voice, model=model)
    # play(audio)
    pass