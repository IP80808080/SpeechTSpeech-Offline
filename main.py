import pyaudio
import pyttsx3
import vosk
from gtts import gTTS

from vosk import Model, KaldiRecognizer
engine = pyttsx3.init()
model = Model(r"K:\Projects\Programming\Python\Extra\Library\Speech Recognition\Vosk\vosk-model-small-en-in-0.4")
model1 = Model(r"K:\Projects\Programming\Python\Extra\Library\Speech Recognition\Vosk\vosk-model-small-hi-0.22")
recognizer = KaldiRecognizer(model or model1, 16000)

list1 = ["what is your name", "who are you", "what are you", "Hi", "Bye", 'How are you']
list2 = ["my name is Lucifer", "I am robo v1.o", "I am a Bot", "Hello", "Bye", "fine and you"]

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


def listen(i):
    engine.say(i)
    engine.runAndWait()
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 150)

def speak(tex):
    for i, j in zip(list1, list2):
        if i == tex:
            print(j)
            listen(j)


while True:

    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text1 = text[14:-3]
        print(text1)
        speak(text1)







