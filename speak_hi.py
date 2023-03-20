import pyttsx3
def speak_hi():
    engine = pyttsx3.init()
    engine.say("Привет!")
    engine.runAndWait()