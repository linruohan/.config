#coding=utf-8
from selenium import webdriver
import os,time
'''用户名数据'''
source = open("F:\\atom\\project\\testdata\\login_name.txt", "r")
username = source.readlines()
source.close()
'''密码数据'''
source = open("F:\\atom\\project\\testdata\\login_passwd.txt", "r")
passwd = source.readlines()
source.close()
browser = webdriver.Chrome()

for str in username :
    browser.get("http://www.baidu.com")
    browser.find_element_by_id("kw").send_keys(str)
    browser.find_element_by_id("su").click()
    browser.back()
browser.quit()
