import pyaudio
import pyttsx3
import vosk
from gtts import gTTS

from vosk import Model, KaldiRecognizer
engine = pyttsx3.init()
model = Model(r"K:\Projects\Programming\Python\Extra\Library\Speech Recognition\Vosk\vosk-model-small-en-in-0.4")
model1 = Model(r"K:\Projects\Programming\Python\Extra\Library\Speech Recognition\Vosk\vosk-model-small-hi-0.22")
recognizer = KaldiRecognizer(model or model1, 16000)

dicte = {
"what is your name":"my name is Lucifer",
"who are you":"I am robo v1.o"

}

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


def listen(i):
    engine.say(i)
    engine.runAndWait()
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 150)

def speak(tex):
    if tex in dicte:
        listen(dicte[tex])
    if tex == "okay stop":
        raise SystemExit



while True:

    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text1 = text[14:-3]
        print(text1)
        speak(text1)







