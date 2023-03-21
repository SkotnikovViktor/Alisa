import pyttsx3
import os

def speak_hi():
    engine = pyttsx3.init()
    engine.say("Да, я здесь и готов вам помочь.")
    engine.runAndWait()

def understent():
    engine = pyttsx3.init()
    engine.say("Скажите вашу команду по другому.")
    engine.runAndWait()


def error():
    engine = pyttsx3.init()
    engine.say("Товарищ, вышла какая-то не известная ошибка.")
    engine.runAndWait()


