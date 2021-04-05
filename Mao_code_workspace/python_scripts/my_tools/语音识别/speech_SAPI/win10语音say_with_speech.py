# _*_ coding:utf-8 _*_

import os
import sys
import speech
import webbrowser

phrase = {
    "closeMainSystem": "关闭人机交互",
    "film": "我要看电影",
    "listenMusic": "我好累啊",
    "blog": "看博客",
    "cmd": "cmd"
}


def callback(phr, phrase):
    if phr == phrase["closeMainSystem"]:
        speech.say("Goodbye. 人机交互即将关闭，谢谢使用")
        speech.stoplistening()
        sys.exit()
    elif phr == phrase["film"]:
        speech.say("正在为您打开优酷")
        webbrowser.open_new("http://www.youku.com/")
    elif phr == phrase["listenMusic"]:
        speech.say("即将为你启动豆瓣电台")
        webbrowser.open_new("http://douban.fm/")
    elif phr == phrase["blog"]:
        speech.say("即将进入Dreamforce.me")
        webbrowser.open_new("http://www.cnblogs.com/darksouls/")
    elif phr == phrase["cmd"]:
        speech.say("即将打开CMD")
        os.popen("C:/Windows/System32/cmd.exe")

    # 可以继续用 elif 写对应的自制中文库中的对应操作


while True:
    phr = speech.input()
    print(phr,'===========')
    speech.say("You said %s" % phr)
    callback(phr, phrase)
