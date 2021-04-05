#coding=utf-8
'''
Created on 2017-9-11
在通知公告中添加通知公告功能
里面的关键词输入可以做成参数化
@author: huojun
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Public.Login
from time import *
driver = webdriver.Chrome()
#调用登陆模块，登陆系统
Public.Login.login(driver)
#点击通知公告菜单，进入通知公告功能
# sleep(2) 通过显示等待方法来替代了sleep命令
element = WebDriverWait(driver,1,).until(
                                         EC.presence_of_element_located
                                         (
                                          (By.XPATH,"//*[@id='menu_151028103050103f8bf46b5b5331e486']/p")
                                          )
                                         )
driver.find_element_by_xpath(".//*[@id='menu_151028103050103f8bf46b5b5331e486']/p").click()

print("进入公告管理功能")
sleep(3)
#点击添加按钮，进入添加通知公告页面
driver.find_element_by_xpath(".//*[@id='151028103114295482d67731f0795a60']/a").click()
sleep(1)
# #添加通知公告信息
print ("添加通知公告信息")
#开始来获取iframe页面
driver.switch_to_frame('content-frame')
driver.find_element_by_xpath(".//*[@id='content_body']/div[4]/div/div[1]/div/button[1]").click()
print("进入添加通知公告页面")
#进行公告标题添加
element = WebDriverWait(driver,1,).until(
                                         EC.presence_of_element_located
                                         (
                                          (By.XPATH,".//*[@id='noticeTitle']")
                                          )
                                         )
driver.find_element_by_xpath(".//*[@id='noticeTitle']").send_keys("公告标题添加")
print("标题添加")
#定位到时间控件元素
driver.find_element_by_xpath(".//*[@id='noticeEnd']").click()
print("选择时间日期")
print(ctime())
#定义js，去掉其只读特性
js = "document.getElementById('noticeEnd').removeAttribute('readonly')"
#执行调用js的命令
driver.execute_script(js)
#在时间窗口输入日期值
driver.find_element_by_id("noticeEnd").send_keys("2017-09-25")
print(ctime())
print("结束时间选择")
#关键词输入
driver.find_element_by_id("noticeKeyword").click()
driver.find_element_by_id("noticeKeyword").send_keys("关键词输入")
print("关键词输入")
#定义edit arae 区域的js
js1 = "UE.getEditor('noticeContent').setContent('霍晓军')"
driver.execute_script(js1)
print("添加完成")
sleep(3)
#点击保存按钮进行保存
driver.find_element_by_xpath(".//*[@id='inputForm']/div[2]/button").submit()
sleep(5)
Public.Login.logout(driver)
