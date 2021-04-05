#coding=utf-8
from selenium import webdriver
import time
'''前进和后退'''
browser=webdriver.Chrome()
browser.set_window_size(480,800)#设置浏览器窗口大小
time.sleep(3)
browser.maximize_window()#浏览器最大化
firsturl='http://www.baidu.com'
seconurl='http://news.baidu.com'
browser.get(firsturl)
browser.get(seconurl)
browser.back()#page 后退
browser.forward()#page 前进
time.sleep(3)
browser.close()
