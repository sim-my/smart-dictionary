from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
#function to convert text to speech and play the sound
def talk(audio):
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-us')
        text_to_speech.save('audio.mp3')
        playsound("audio.mp3")
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say')
        audio = r.listen(source)
    try: 
        command = r.recognize_google(audio).lower()
        talk('You said: ' + command + '\n')
    except sr.UnknownValueError:
        talk('Your last command couldn\'t be heard')

myCommand()

