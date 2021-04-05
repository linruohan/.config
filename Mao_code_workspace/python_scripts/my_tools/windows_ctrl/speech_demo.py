# 将输入文字转化为语音信号输出
import speech

while True:
    speech.say("请输入：")
    str = input("请输入：")
    speech.say("你输入的内容是: ")
    speech.say(str)