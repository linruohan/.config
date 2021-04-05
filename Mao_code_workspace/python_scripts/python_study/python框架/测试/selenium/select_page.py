#coding=utf-8
'''测试-ing'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys #模拟键盘输入。

url='http://193.169.100.247:8080/itmsv2mdj/'
username='admin'
passwd='admin'

driver=webdriver.Chrome()
driver.maximize_window()
sleep(2)
driver.get(url)
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(passwd)
sleep(2)
# driver.find_element_by_id('password').send_keys(Keys.RETURN)
driver.find_element_by_xpath('//input[@class="btn"]').submit()
driver.quit()
