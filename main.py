import requests
from difflib import get_close_matches 
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import os

def talk(audio):    
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        playsound("audio.mp3")
        os.remove("audio.mp3")

def translate(word):
    talk('The meanings of'+word+'are')
    response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word)
    data = response.json()
    for definition in data[0]['meanings'][0]['definitions']:
        talk(definition["definition"])




#function to convert text to speech and play the sound
def dictionaryCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try: 
        command = r.recognize_google(audio).lower()
        talk('You said: ' + command)
    except sr.UnknownValueError:
        talk('Your last command couldn\'t be heard')
        askMeaningOrNOt()
    return command

def welcome():
    talk('Welcome to easy dictionary')

def askMeaningOrNOt():
    talk('Do you wanna ask meaning of any word? Answer in yes or no.')
    answer = dictionaryCommand()
    if(answer == 'yes'):
        giveWord()
    elif(answer == 'no'):
        exit()
    else:
        talk('I\'m sorry. I don\'t know what to do.')
        askMeaningOrNOt()

def giveWord():
    talk('Say the word')
    word = dictionaryCommand()
    translate(word)
    askMeaningOrNOt()

def exit():
    talk('Thanks for using easy dictionary')

welcome()
askMeaningOrNOt()