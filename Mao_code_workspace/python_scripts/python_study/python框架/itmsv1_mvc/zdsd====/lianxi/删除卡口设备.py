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
print(number0)
# driver.switch_to.default_content()

#找到名称为key的卡口设备并删除
key=u'的萨芬'
knames=s.findsXpath(driver,'//tbody[@id="tbody"]/tr/td[2]')
kname=[kname.text for kname in knames]
kindex=[kname.index(i) for i in kname if key in i]
s.findXpath(driver,("//*[@id='rowcount"+str(kindex[0])+"']/td[9]/a[3]")).click()

#点击确认删除alert
del_alert=driver.switch_to_alert()
print(del_alert.text)
del_alert.accept()
# del_alert.dismiss()#取消删除
#验证长安路设备数量
time.sleep(3)
number1=s.findCss(driver,'#content_body > div > div > div.page_info > b:nth-child(3)').text
print("number1="+number1)
if int(number0)-int(number1)==1:
    print(number0+'-'+number1+'=1')
    s.jietu(driver)
    print(u'successfully added！成功删除一条数据')
else:
    print(u'sorry，删除失败')

print(u'设备信息删除成功！')




driver.quit()
