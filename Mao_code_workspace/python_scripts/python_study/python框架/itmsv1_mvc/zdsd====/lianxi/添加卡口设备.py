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
#设备管理——卡口设备——添加
s.findXpath(driver,'//*[@id="130502094519328f815bc3af1d635903"]/a').click()
# driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
driver.switch_to_frame('content-frame')
time.sleep(2)
s.findId(driver,'tree-rec_3_a').click()

driver.switch_to_frame('myIframe')
number0=s.findXpath(driver,'//div[@class="page_info"]/b[3]').text
driver.switch_to.default_content()
driver.switch_to_frame('content-frame')
time.sleep(2)
s.findClassName(driver,'icon-plus').click()
driver.switch_to_frame('myIframe')
time.sleep(2)
#基本信息
js = 'document.getElementById("orgNames").removeAttribute("readonly");'
driver.execute_script(js)
s.findId(driver,'orgNames').click()
time.sleep(1)
s.findXpath(driver,'//*[@id="orgTreeSpace_2_span"]').click()
s.findXpath(driver,'//*[@id="tab1"]/div[1]/table/tbody/tr[3]/td[2]/div/button').click()
s.findXpath(driver,'//*[@id="dropdown-ul"]/li[1]').click()
s.findId(driver,'name').send_keys(sj_hz.s())
time.sleep(2)
s.findId(driver,'deviceTypeNames').click()
time.sleep(2)
s.findId(driver,'dtTreeSpace_2_span').click()
s.findId(driver,'pattern').send_keys(sj_8str.s())
#环境配置
s.findXpath(driver,'//*[@id="inputForm"]/ul/li[2]/a').click()
time.sleep(2)
s.findId(driver,'ip').send_keys(sj_IP.s())
s.findId(driver,'timeout').send_keys(sj_3.s())
#方向配置
time.sleep(2)
s.findXpath(driver,'//*[@id="inputForm"]/ul/li[3]/a').click()
s.findCss(driver,'#directionCode_01').click()
time.sleep(2)
#建设信息
s.findXpath(driver,'//*[@id="inputForm"]/ul/li[4]/a').click()
s.findXpath(driver,'//*[@id="companyId_chzn"]/a/span').click()
s.findId(driver,'companyId_chzn_o_2').click()
time.sleep(2)

#保存
confire=s.findId(driver,'submit_btn')
driver.execute_script("arguments[0].scrollIntoView();", confire)#元素聚焦
confire.click()
time.sleep(2)

#验证长安路设备数量
number1=s.findCss(driver,'#content_body > div > div > div.page_info > b:nth-child(3)').text
if int(number1)-int(number0)==1:
    print(number1+'-'+number0+'=1')
    print(u'successfully added！成功添加一条数据')
else:
    print(u'sorry，添加失败')


driver.quit()
