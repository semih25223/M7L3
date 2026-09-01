
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

duration = 5
sample_rate = 44100

lang = input("Hangi dile çevirmeliyim? (it=İtalyanca, es=İspanyolca, en=İngilizce, de=Almanca): ")

print("Şimdi konuşun...")

recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

wav.write("output.wav", sample_rate, recording)
print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

recognizer = sr.Recognizer()

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="tr")
    print("Şunu söylediniz:", text)

    translator = Translator()
    translated = translator.translate(text, dest=lang)

    print("🌍 Çeviri:", translated.text)

except sr.UnknownValueError:
    print("Konuşma tanınamadı.")

except sr.RequestError as e:
    print(f"Hizmet hatası: {e}")