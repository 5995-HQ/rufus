# This is Rufus, it's a bot that knows all and can do everything.

import speech_recognition as sr
import os
import sys
import datetime
import warnings
import calendar
import random
import re
import wikipedia
import webbrowser

from gtts import gTTS

warnings.filterwarnings("ignore")

microphone = sr.Microphone()

def recordAudio():
    r = sr.Recognizer()
    with microphone as source:
        audio = r.listen(source)
        print(audio)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

bye_words = ["exit", "quit", "okay bye", "goodbye", "bye", "see you later", "see ya later", "cya", "ttyl", "ttya"]
hi_words = ["hello", "Hi there", "hi" "hey", "hello", "hiya", "hey there", "heyya", "hey", "hello there", "hey hey"]

print("\n" + "#"*20 + " Say something " + "#"*20 + "\n")
while True:
    words = recordAudio()
    words
    if words in hi_words:
        os.system(f'{random.choice(hi_words)}')
        break
    if words in bye_words:
        print("\n" + "#"*20 + " Bye " + "#"*20 + "\n")
        exit(1)
    if "hey Rufus open a Google search for" in words:
        words = words.replace("hey Rufus open a Google search for", "")
        endwords = words.strip().replace(" ","+")
        os.system(f'say -v Daniel "searching for {words.strip()}"')
        webbrowser.open(f"https://www.google.com/search?q={endwords}")
    if "hey Rufus" or "a Rufus" or "Rufus" and "who is" or "when is" or "when did" or "why is" or "what is" in words:
        words = words.replace("hey Rufus", "")
        words = words + "?"
        print(words)
        os.system(f'say -v Daniel "searching for {words.strip()}"')
        try:
            os.system(f'say -v Daniel "{wikipedia.summary(words, sentences=1)}."')
            break
        except wikipedia.exceptions.DisambiguationError as e:
            cleanup = re.sub(r'^.*?(is|did)', '', words)
            potentials = potentials = wikipedia.search(cleanup)
            os.system(f'say -v Daniel "I found {potentials}. Which one sounds good to you?"')
            break
    
    else:
        os.system(f'say -v Daniel "I couldn\'t find anything on that."')
