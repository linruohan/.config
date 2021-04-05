#coding=utf-8

from selenium import webdriver

b=webdriver.Chrome()
b.get('http://www.baidu.com')
cookie=b.get_cookies()
print (cookie)
b.close()
