# This is Rufus, it's a bot that knows all and can do everything.

import speech_recognition as sr
import os
import sys
import datetime
import warnings
import calendar
import random
import wikipedia
import webbrowser

from gtts import gTTS

warnings.filterwarnings("ignore")

microphone = sr.Microphone()

def recordAudio():
    r = sr.Recognizer()
    with microphone as source:
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    os.system(f'say "{data}"')
    return data

recordAudio()