# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha  # 网速较慢，难以使用
import os
import sys

engine = pyttsx3.init('sapi5')  # 发出声音
# WolframAlpha是开发计算数学应用软件的沃尔夫勒姆研究公司开发出的新一代的搜索引擎,能根据问题直接给出答案的网站
client = wolframalpha.Client('Your_App_ID')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print(audio)
    try:
        query = r.recognize_google(
            audio, language="cmn-Hans-CN", show_all=True)
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query


def main():
    greetMe()
    speak('Hello Sir, I am your digital assistant LARVIS the Lady Jarvis!')
    speak('How may I help you?')
    while True:
        query = myCommand().lower()
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!',
                      'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username',
                                    "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'hello' in query:
            speak('Hello Sir')
        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'play music' in query:
            music_folder = 'D:\Music\剧情'
            music = ['', '', '', '', '']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')
        else:
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    # speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
            except:
                webbrowser.open('www.google.com')
        speak('Next Command! Sir!')


if __name__ == '__main__':
    main()
