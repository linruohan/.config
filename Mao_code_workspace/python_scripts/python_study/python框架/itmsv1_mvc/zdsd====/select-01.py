#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,UnexpectedTagNameException
from selenium.webdriver.support.ui import Select
from time import sleep
import sys,time
# sys.path.append('E:\\atom\\Python\\itmsv1\\zdsd====\\卡口设备状态.html')

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('file:///E:/atom/Python/itmsv1/zdsd====/卡口设备状态.html')
select=Select(driver.find_element_by_id('selectMethod'))
time.sleep(2)
select.select_by_index(2)
time.sleep(3)
select.select_by_value('python')
time.sleep(3)
select.select_by_visible_text(u'python语言')

time.sleep(3)

print(select.all_selected_options[0])
print(select.first_selected_option)

driver.quit()
