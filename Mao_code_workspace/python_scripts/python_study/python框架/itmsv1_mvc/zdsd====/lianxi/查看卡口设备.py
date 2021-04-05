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

#进入卡口系统
s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
time.sleep(2)
#设备管理——卡口设备——查看
s.findXpath(driver,'//*[@id="130502094519328f815bc3af1d635903"]/a').click()
# driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
driver.switch_to_frame('content-frame')
time.sleep(2)
s.findId(driver,'tree-rec_3_a').click()
driver.switch_to_frame('myIframe')

key=u'的萨芬'
knames=s.findsXpath(driver,'//tbody[@id="tbody"]/tr/td[2]')
kname=[kname.text for kname in knames]
kindex=[kname.index(i) for i in kname if key in i]
s.findXpath(driver,("//*[@id='rowcount"+str(kindex[0])+"']/td[9]/a[1]")).click()
print(u'设备信息查看成功！')



driver.quit()
