import datetime
import pyaudio
import pyttsx3
import vosk
from vosk import Model, KaldiRecognizer
from time import strftime

engine = pyttsx3.init('sapi5')
model = Model(r"C:\Users\gaura\PycharmProjects\robot\vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def listen(i):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',130)
    engine.say(i)
    engine.runAndWait()




def speak(tex):
    if tex == "okay stop":
        listen("okay")
        raise SystemExit
    elif tex == "showtime":
        string = strftime('%H:%M')
        now = datetime.datetime.now().time()
        if 12 >= now.hour > 6:
            listen("Good morning")
            print(string)
            listen("its"+string)
        elif 17 >= now.hour > 12:
            listen("Good afternoon")
            print(string)
            listen("its"+string)
        elif 21 >= now.hour > 17:
            listen("Good Evening")
            print(string)
            listen("its"+string)
        elif 00 >= now.hour > 21:
            listen("Good night")
            print(string)
            listen("its"+string)
        else:
            listen(string)
    elif tex == "today's date":
        date = datetime.datetime.now()
        listen(f'{date:%b %d %Y}')
    elif tex == "hi":
        listen("Hello")
    elif tex == "who are you":
        listen("I am sika the robo")
    elif tex == "my college":
        listen("shri sant gajanan maharaj college of engineering ssgmce")
    elif tex == "head of computer science":
        listen("doctor s b patil")
    elif tex == "head of electrical engineering":
        listen("Doctor S R Paraskar")
    elif tex == "head of information technology":
        listen("Doctor A S Maanekar")
    elif tex == "head of electronics":
        listen("Doctor M N Tibdewal")
    elif tex == "head of applied science and humanities":
        listen("Doctor N A Patil")
    elif tex == "head of mechanical engineering":
        listen("Doctor S P Trikaal")
    elif tex == "thanks":
        listen("its my pleasure")
    elif tex == "name of our library":
        listen("pradnya chakshu gulaabraao granthalayaa")
    elif tex == "principal of our college":
        listen("doctor s b somaani")

while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text1 = text[14:-3]
        print(text1)
        speak(text1)
