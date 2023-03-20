import speech_recognition as sp
import pyaudio
import pygame 

pygame.init()
pygame.mixer.init()

mic = sp.Microphone(device_index=3)

r = sp.Recognizer()
with sp.Microphone() as source:
    print("Скажи что-нибудь")
    audio = r.listen(source)

try:
    a = r.recognize_google(audio, language="ru-RU")
    print("Вход. " + a)
except sp.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sp.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


if a=="Привет":
    pygame.mixer.music.load("hi.mp3")
    pygame.mixer.music.play(-1)
else:
    print("Я вас не понял.")
    
