#coding=utf-8

from selenium import webdriver
b=webdriver.Chrome()
b.get('http://www.baidu.com')

try:
    b.find_element_by_id("kwss").send_keys("selenium")
    b.find_element_by_id("su").click()
except Exception as e:
    b.get_screenshot_as_file(os.path.dirname(__file__)+"/123.png")#拍照片报错
b.quit()
