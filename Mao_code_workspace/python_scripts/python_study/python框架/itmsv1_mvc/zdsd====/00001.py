#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time, re,sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out
s=find
driver = webdriver.Firefox()
# driver.implicitly_wait(10)
driver.maximize_window()
base_url = "http://193.169.100.249:8086/itmsld/"
driver.get(base_url)
s.findId(driver,'username').clear()
s.findId(driver,'password').clear()
s.findId(driver,'username').send_keys('admin')
s.findId(driver,'password').send_keys('admin')
s.findXpath(driver,'//input[@value="登 录"]').submit()
time.sleep(2)
print('admin，温馨提示，您已成功登陆平台！')
s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
time.sleep(2)
s.findXpath(driver,'//*[@id="1404161355392917afeff9583374f9a1"]/a').click()
driver.switch_to_frame('content-frame')
time.sleep(2)
s.findId(driver,'tree-rec_3_a').click()
s.findId(driver,'addImg').click()
driver.switch_to_frame('myIframe')
time.sleep(2)
# s.findId(driver,'submit_btn').click()
# element = WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located((By.ID,"submit_btn")))
# element.find_element_by_id("submit_btn").click()
print('sdf')
