# *_*coding:utf-8 *_* 
import time,pyperclip
import os,sys,re,win32com.client
speaker = win32com.client.Dispatch("SAPI.SPVOICE")
recent_value = ""
while True:
    tmp_value = pyperclip.paste()  # 读取剪切板复制的内容
    try:
        if tmp_value != recent_value:  # 如果检测到剪切板内容有改动，那么就进入文本的修改
            print(tmp_value)
            recent_value = tmp_value
            speaker.Speak(tmp_value)
    except KeyboardInterrupt:  # 如果有ctrl+c，那么就退出这个程序。  （不过好像并没有用。无伤大雅）
        break
    if tmp_value == 'end':  # 如果复制的是getend，就退出程序。（这个主要是为了方便我在spyder中运行、退出的时候用的。）
        break
