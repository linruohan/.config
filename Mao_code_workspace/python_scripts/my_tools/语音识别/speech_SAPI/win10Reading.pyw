# coding=utf-8

import win32com.client
import sys
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = 1
speaker.Volume = 100
"""win10 阅读器"""
try:
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        # with open('test.txt', 'r',encoding='utf-8') as f:
        for i in f.readlines():
            speaker.Speak(i)
except Exception as e:
    print(e)
    speaker.Speak("启动失败")
