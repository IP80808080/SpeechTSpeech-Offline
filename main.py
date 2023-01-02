import datetime
import pyaudio
import pyttsx3
import vosk
from vosk import Model, KaldiRecognizer
from time import strftime
import datetime as dt
engine = pyttsx3.init()
model = Model(r"C:\Users\gaura\PycharmProjects\robot\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
def listen(i):
    engine.say(i)
    engine.runAndWait()
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 150)
def speak(tex):
    if tex == "okay stop":
        raise SystemExit
    elif tex == "showtime":
        string = strftime('%H:%M')
        now = datetime.datetime.now().time()
        if  12>=now.hour>6:
            listen("Good morning")
            print(string)
            listen("its"+string)
        elif 17>=now.hour>12:
            listen("Good afternoon")
            print(string)
            listen("its"+string)
        elif 21>=now.hour>17:
            listen("Good Evening")
            print(string)
            listen("its"+string)
        elif 00>=now.hour>21:
            listen("Good night")
            print(string)
            listen("its"+string)
        else:
            listen(string)
    elif tex == "who are you":
        listen("I am robo v1.o")
    elif tex ==  "who is the head department of computer science":
        listen("Doctor s b Patil")
    elif tex ==  "who is the head department of electrical engineering":
        listen("Doctor S R Paraskar")
    elif tex ==  "who is the head department of information technology":
        listen("Doctor A S Manekar")
    elif tex ==  "who is the head department of electronics and telecommunication engineering":
        listen("Doctor M N Tibdewal")
    elif tex ==  "who is the head department of applied sciences and humanities":
        listen("Doctor N A Patil")
    elif tex ==  "who is the head department of mechanical engineering":
        listen("Doctor S P Trikal")
    elif tex ==  "my college":
        listen("shri sant gajanan maharaj college of engineering shegon")
    
    elif tex ==  "my branch":
        listen("computer science and engineering")

while True:
    data = stream.read(4096,exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text1 = text[14:-3]
        print(text1)
        speak(text1)
