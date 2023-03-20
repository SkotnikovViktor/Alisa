import pyttsx3
import os

def speak_hi():
    engine = pyttsx3.init()
    engine.say("Так точно сэр!")
    engine.runAndWait()
def understent():
    engine = pyttsx3.init()
    engine.say("Сэр, я вас не понял.")
    engine.runAndWait()