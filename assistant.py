import time
import pyttsx3 as p
import webbrowser
import wikipedia
import speech_recognition as sr
from datetime import datetime as d

engine =p.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listen...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("record...")
        query=r.recognize_google(audio,language="hn-in")
        print(query)
    except Exception as e:
        print("try again!")
        return "None"
    return query

print("Can we continue press Enter.\n for exit speak 'exit'")

speak("Hello Prashant, how can i help you?")

while(1):

    q="shivaji maharaj wikipedia"

    if "open google" in q:
        webbrowser.open("google.com")
        speak("google is open now")

    elif "open youtube" in q:
        webbrowser.open("youtube.com")

    elif "my name" in q :
        print("Prashant Patil")
        speak("You are name is prashant patil")

    elif "wikipedia" in q:
        results=wikipedia.summary(q,sentences=2)
        print(results)
        speak(results)

    elif "exit" in q:
        speak("Ok bye, meet again")
        break

    elif "time" in q:
        ctime = d.now()
        speak(ctime)

    else :
        speak("I can not understant please speak again!")


    time.sleep(1)