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
    # os.system(f'say "{data}"')
    return data

words = recordAudio()
words
if "hey Rufus open a Google search for" in words:
    print(words)
    words = words.replace("hey Rufus open a Google search for", "")
    endwords = words.strip().replace(" ","+")
    os.system(f'say -v Daniel "searching for {words.strip()}"')
    webbrowser.open(f"https://www.google.com/search?q={endwords}")
else:
    os.system(f'say -v Daniel "{words}"')