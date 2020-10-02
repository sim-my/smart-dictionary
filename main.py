import requests
from difflib import get_close_matches 
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import os

# def talk(audio):    
#     for line in audio.splitlines():
#         text_to_speech = gTTS(text=audio, lang='en-us')
#         text_to_speech.save('audio.mp3')
#         playsound("audio.mp3")
#         os.remove("audio.mp3")

def translate(word):
    response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word)
    print(response.json())

translate('boastful')

#function to convert text to speech and play the sound


# def myCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         talk('Say a word')
#         audio = r.listen(source)
#         talk('Okay')
#     try: 
#         command = r.recognize_google(audio).lower()
#         talk('You said: ' + command + '\n')
#     except sr.UnknownValueError:
#         talk('Your last command couldn\'t be heard')

# myCommand()

