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
driver.switch_to.frame('content-frame')
time.sleep(2)
s.findId(driver,'tree-rec_2_span').click()
#输入查询条件
name='阿斯顿'
s.findXpath(driver,'//*[@id="s_name"]').send_keys(name)
s.findXpath(driver,'//*[@id="s_code"]').send_keys('522728000001011013')
Select(s.findId(driver,"dev-select")).select_by_value('1708021631148488b93e')
"""
<option value="1708021631148488b93e">西安详讯</option>
<option value="170803143742659d109f">银江股份</option>
<option value="17092009274439868d31">西安详讯</option>
<option value="170803143721033f3a29">海康威视</option>
"""
Select(s.findId(driver,"selXSF")).select_by_value('01')
'''
<option value="01">闯红灯</option>
<option value="02">公路卡口设备</option>
<option value="03">测速设备</option>
<option value="04">闭路电视</option>
<option value="05">移动摄像</option>
<option value="06">警务通</option>
<option value="07">区间测速</option>
<option value="08">卫星定位装置</option>
<option value="09">其它电子设备</option>
'''
s.findXpath(driver,'//*[@id="deviceTypeNames"]').click()
s.findXpath(driver,'//*[@id="dtTreeSpace_2_span"]').click()
s.findXpath(driver,'//*[@id="dtTreeSpace_5_check"]').click()
time.sleep(2)
s.findXpath(driver,'//*[@id="orgNames"]').click()
s.findXpath(driver,'//*[@id="orgTreeSpace_2_span"]').click()
time.sleep(2)
s.findXpath(driver,'//*[@id="s_ip"]').send_keys('120.20.30.35')

#開始查詢
s.findXpath(driver,'//*[@id="content_body"]/div[4]/div[1]/form/table/tbody/tr[2]/td[8]/input[1]').click()
time.sleep(2)



driver.switch_to.frame('myIframe')
number0=s.findXpath(driver,'//div[@class="page_info"]/b[3]').text
print(u'查詢結果：一共有'+number0+'條卡口數據')
dname=s.findXpath(driver,'//*[@id="rowcount0"]/td[2]').text
if name==dname:
    print(u'查詢成功！')
else:
    print(u'查詢失敗')
#重置查詢
driver.switch_to.default_content()
driver.switch_to.frame('content-frame')
time.sleep(2)
s.findXpath(driver,'//*[@id="content_body"]/div[4]/div[1]/form/table/tbody/tr[2]/td[8]/input[2]').click()
s.findXpath(driver,'//*[@id="content_body"]/div[4]/div[1]/form/table/tbody/tr[2]/td[8]/input[1]').click()
time.sleep(2)
driver.switch_to.frame('myIframe')
number1=s.findXpath(driver,'//div[@class="page_info"]/b[3]').text
print(u'重置後，一共有'+number1+'條卡口數據')

driver.quit()
