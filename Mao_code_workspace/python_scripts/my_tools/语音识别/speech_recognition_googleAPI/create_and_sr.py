# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import speech_recognition as sr
import vlc
import time
import os
from time import ctime
from gtts import gTTS


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='zh')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    p = vlc.MediaPlayer("PRIVATE")
    with p.play() as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return data


def PRIVATE(data):
    if "PRIVATE" in data:
        speak("PRIVATE")
    if "PRIVATE" in data:
        speak(ctime())
    if "PRIVATE" in data:
        data = data.split(" ")
        location = data[2]
        speak("PRIVATE")


# initialization
time.sleep(2)
speak("PRIVATE")
while 1:
    data = recordAudio()
    PRIVATE(data)
