#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,sys,io,string
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out,sj_IP,sj_8str,sj_hz,sj_3
s=find

driver =login_in_out.login()

# 获得 cookie信息
cookie_list = driver.get_cookies()
print (cookie_list)
