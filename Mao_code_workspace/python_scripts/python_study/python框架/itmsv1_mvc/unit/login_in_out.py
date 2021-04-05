#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,sys,io
import sys
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from itmsv1.unit import find
s=find

def login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    base_url = "http://193.169.100.249:8086/itmsld/"
    # base_url = ""
    # base_url = "http://193.169.100.238:8086/itmsld/"
    # base_url = "http://193.169.100.249:8083/itmsyangling/"
    # base_url = "http://193.169.100.224:8080/itmsyangling/home/admin/#"

    driver.get(base_url)
    s.findId(driver,'username').clear()
    s.findId(driver,'password').clear()
    s.findId(driver,'username').send_keys('admin')
    s.findId(driver,'password').send_keys('admin')
    s.findXpath(driver,'//input[@value="登 录"]').submit()
    time.sleep(2)
    sname=s.findXpath(driver,'//*[@id="dropdown-toggle"]/span[1]').text

    if sname==u'超级管理员':
        print(u'log in！go on...')
    else:
        print(u'登录失败！')
    return driver
def quit(driver):
    s.findClassName(driver,'caret').click()
    time.sleep(1)
    s.findXpath(driver,'//*[@id="dropdown-menu"]/li[2]/a').click()
    driver.close()
    print(u'admin，温馨提示，您已成功退出平台！')

if __name__ == '__main__':
    driver=login()
    quit(driver)
