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

def wish_me():
    hour = (dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sartaj. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon Sartaj. How are you doing")

    else:
        speak("Good evening Sartaj. How are you doing")
    
    speak("I am JARVIS. Tell me Sartaj how can i help you")

# speak('We are developing Desktop Assistant Project')
#text = takeCommand()
#speak(text)

if __name__ == '__main__':
     
    wish_me()

    while True:

        print('Please ask...')
        query = takeCommand().lower()
        print(query)

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query=query.replace('wikipedia','')
            results = wp.summary(query,sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'youtube' in query:
            speak('Opening Youtube')
            wb.open('youtube.com')
        elif 'google' in query:
            speak('Opening Google')
            wb.open('google.com')        
        elif 'good by' in query:
            exit()