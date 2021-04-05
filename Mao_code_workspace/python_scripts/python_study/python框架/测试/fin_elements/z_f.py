# -*- coding: utf-8 -*-
from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get(os.getcwd()+'\\'+'z_f.html')
# 1.xpath: `.`代表当前节点; '..'代表父节点
print driver.find_element_by_xpath("//div[@id='C']/../..").text

# 2.xpath轴 parent
print driver.find_element_by_xpath("//div[@id='C']/parent::*/parent::div").text
driver.quit()
