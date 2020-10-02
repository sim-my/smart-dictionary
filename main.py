from gtts import gTTS
import speech_recognition as sr
from playsound import playsound

#function to convert text to speech and play the sound
def talk(audio):
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        playsound("audio.mp3")

talk('Hey! I am Easy Dictionary.')