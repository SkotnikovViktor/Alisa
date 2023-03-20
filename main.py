import speech_recognition as sp
from speak_hi import *

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
    speak_hi() 
    print("Выход: --->")
else:
    print("Я вас не понял.")
    
