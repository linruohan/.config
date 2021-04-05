# -*- coding: utf-8 -*-
from selenium import webdriver
import win32gui
import win32con
import time

'''
多文件上传
'''

dr = webdriver.Firefox()
dr.get('http://www.sucaijiayuan.com/api/demo.php?url=/demo/20150128-1')

dr.switch_to.frame('iframe')  # 一定要注意frame
'''点击打开，文件选择框'''
dr.find_element_by_class_name('filePicker').click()
time.sleep(1)


dialog = win32gui.FindWindow('#32770', None)
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)

# 跟上面示例的代码是一样的，只是这里传入的参数不同，如果愿意可以写一个上传函数把上传功能封装起来
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, '"d:\\baidu.py" "d:\\upload.py" "d:\\1.html"')
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


print dr.find_element_by_id('status_info').text
dr.quit()
