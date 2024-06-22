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
    ''' This function takes text and returns voice
    Args : speak(_type_) String'''
    engine.say(text)
    engine.runAndWait()

# Speach Recognization function
def takeCommand():
    ''' This function will recognize voice and return text'''
    r = sr.Recognizer()
    with sr.Microphone() as source:   # Open the microphone
        print("Listening")
        r.pause_threshold = 1       # Pause the threshold for 1 mili seconds
        audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language = 'en-in')
            print(f'User said: {query}\n')
        except Exception as e:
            print('Could not listen properly : Please say it again !')
            return None
        return query


# speak('We are developing Desktop Assistant Project')
text = takeCommand()
speak(text)