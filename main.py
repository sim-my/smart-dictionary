#import the necessary libraries
import requests
from difflib import get_close_matches 
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import os

#converts text to audio
def talk(text):    
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        playsound("audio.mp3")
        os.remove("audio.mp3")

#gives the definitions of the word
def translate(word):
    talk('The meanings of'+word+'are')
    response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word)
    data = response.json()
    for definition in data[0]['meanings'][0]['definitions']:
        talk(definition["definition"])

#Asks for command
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

#welcome greeting
def welcome():
    talk('Welcome to easy dictionary')


#Yes or No for asking meaning
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

#Intermediate function for generating definition of given word
def giveWord():
    talk('Say the word')
    word = dictionaryCommand()
    translate(word)
    askMeaningOrNOt()


#exits from the application
def exit():
    talk('Thanks for using easy dictionary')

#calling necessary functions
welcome()
askMeaningOrNOt()