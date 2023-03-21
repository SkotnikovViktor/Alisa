# Голосовой помошник **
import speech_recognition as sp
import os
from speak_hi import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



# Чекаем микро на сказанные слова
mic = sp.Microphone(device_index=3)
r = sp.Recognizer()
with sp.Microphone() as source:
    print("Скажи что-нибудь")
    audio = r.listen(source)


try:
    spoke_user = r.recognize_google(audio, language="ru-RU")
except sp.UnknownValueError:
    error()
except sp.RequestError as e:
    error()




# Проверка, что сказал пользователь
test = fuzz.ratio("привет" or "приветики" or "здарово" or "ку", spoke_user )
if test >= 50:
    speak_hi()
else:
    understent()


#if spoke_user=="Здесь?":
#    speak_hi() 
#    print("Выход: --->")
#elif spoke_user=="Открой Paint":
#    os.startfile("C:/WINDOWS/system32/mspaint.exe")
#else:
#    understent()    
