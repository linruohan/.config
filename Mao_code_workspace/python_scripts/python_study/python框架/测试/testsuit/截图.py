#coding=utf-8

import local
from selenium import webdriver
import sys,time,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

b=local
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
b.findId(driver,'kw').send_keys('selenium')
time.sleep(2)
b.findId(driver,'su').click()

time.sleep(2)
'''截图功能'''
b.jietu(driver)
driver.quit()
