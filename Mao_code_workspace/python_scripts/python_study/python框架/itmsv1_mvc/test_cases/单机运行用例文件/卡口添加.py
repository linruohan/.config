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
# driver.switch_to.default_content ()
driver.switch_to.frame ('myIframe')
number0 = s.findXpath (driver, '//div[@class="page_info"]/b[3]').text
driver.switch_to.default_content ()
driver.switch_to.frame ('content-frame')
s.findClassName (driver, 'icon-plus').click ()
time.sleep (2)
driver.switch_to.frame ('myIframe')
# 基本信息
js = 'document.getElementById("orgNames").removeAttribute("readonly");'
driver.execute_script (js)
s.findId (driver, 'orgNames').click ()
time.sleep (1)
s.findXpath (driver, '//*[@id="orgTreeSpace_2_span"]').click ()
s.findXpath (driver, '//*[@id="tab1"]/div[1]/table/tbody/tr[3]/td[2]/div/button').click ()
s.findXpath (driver, '//*[@id="dropdown-ul"]/li[1]').click ()
s.findId (driver, 'name').send_keys (sj_hz.s ())
time.sleep (2)
s.findId (driver, 'deviceTypeNames').click ()
time.sleep (2)
s.findId (driver, 'dtTreeSpace_2_span').click ()
s.findId (driver, 'pattern').send_keys (sj_8str.s ())
# 环境配置
s.findXpath (driver, '//*[@id="inputForm"]/ul/li[2]/a').click ()
time.sleep (2)
s.findId (driver, 'ip').send_keys (sj_IP.s ())
s.findId (driver, 'timeout').send_keys (sj_3.s ())
# 方向配置
time.sleep (2)
s.findXpath (driver, '//*[@id="inputForm"]/ul/li[3]/a').click ()
s.findCss (driver, '#directionCode_01').click ()
time.sleep (2)
# 建设信息
s.findXpath (driver, '//*[@id="inputForm"]/ul/li[4]/a').click ()
s.findXpath (driver, '//*[@id="companyId_chzn"]/a/span').click ()
s.findId (driver, 'companyId_chzn_o_2').click ()
time.sleep (2)
