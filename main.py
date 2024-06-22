import pyttsx3 as tts  # Text to speach conversion
import speech_recognition as sr 
import datetime as dt
import wikipedia as wp
import webbrowser as wb
import os

# Takeing voice from my system
engine = tts.init('sapi5')
voices = engine.getProperty('voices')
'''
print(voices) # sapi5 has two List of voices
print(type(voices)) # Type of the object is list
print(voices[0].id) # Male voice
print(voices[1].id) # Female voice
'''

engine.setProperty('voice',voices[0].id)  # For this project lets take Male voice for desktop assistant
engine.setProperty('rate',150)            # Rate of Speed of audio

# Create a speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak('I am Saartaaj')