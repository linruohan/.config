# coding=utf-8
from selenium.webdriver.support.ui import Select
import unittest, time

'''****************************************'''
'''****************************************'''
'''***********卡口设备模块*************'''
'''**************（测试）**********************'''
'''****************************************'''
from itmsv1.unit import find, login_in_out, sj_3, sj_8str, sj_hz, sj_IP

s = find
from selenium import webdriver

driver = webdriver.Chrome ()
driver.maximize_window()
driver.get ('http://193.169.100.249:8086/itmsld/login')
s.findId (driver, 'username').clear ()
s.findId (driver, 'password').clear ()
s.findId (driver, 'username').send_keys ('admin')
s.findId (driver, 'password').send_keys ('admin')
s.findXpath (driver, '//input[@value="登 录"]').submit ()
time.sleep (2)
# 进入卡口系统
s.findId (driver, 'menu_1304261304150253833622fa401af96b').click ()
time.sleep (2)
# 设备管理——卡口设备
s.findXpath (driver, '//*[@id="130502094519328f815bc3af1d635903"]/a').click ()
# driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
driver.switch_to.frame ('content-frame')
time.sleep (2)
s.findId (driver, 'tree-rec_5_a').click ()

driver.switch_to.frame ('myIframe')
time.sleep(2)
key = u'订术正之叨'
es = s.findsXpath (driver, '//tbody[@id="tbody"]/tr/td[2]')
kname = [sm.text for sm in s.findsXpath (driver, '//tbody[@id="tbody"]/tr/td[2]')]
kindex = [kname.index (i) for i in kname if key in i]
s.findXpath (driver, ("//*[@id='rowcount" + str (kindex[0]) + "']/td[9]/a[1]")).click ()
print (u'设备信息查看成功！')