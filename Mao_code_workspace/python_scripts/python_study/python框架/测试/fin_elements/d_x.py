# -*- coding: utf-8 -*-
from selenium import webdriver

import os

driver = webdriver.Chrome()
driver.get(os.getcwd()+'\\'+'d_x.html')

# 1.xpath,通过父节点获取其哥哥节点
print driver.find_element_by_xpath("//div[@id='D']/../div[1]").text

# 2.xpath轴 preceding-sibling
print driver.find_element_by_xpath("//div[@id='D']/preceding-sibling::div[1]").text

driver.quit()
