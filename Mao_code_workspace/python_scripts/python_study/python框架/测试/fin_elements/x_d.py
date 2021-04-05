# -*- coding: utf-8 -*-
from selenium import webdriver

import os

driver = webdriver.Chrome()
driver.get(os.getcwd()+'\\'+'d_x.html')

# 1.xpath，通过父节点获取其弟弟节点
print driver.find_element_by_xpath("//div[@id='D']/../div[3]").text
# 2.xpath轴 following-sibling
print driver.find_element_by_xpath("//div[@id='D']/following-sibling::div[1]").text
# 3.xpath轴 following
print driver.find_element_by_xpath("//div[@id='D']/following::*").text
# 4.css selector +
print driver.find_element_by_css_selector('div#D + div').text
# 5.css selector ~
print driver.find_element_by_css_selector('div#D ~ div').text

driver.quit()
