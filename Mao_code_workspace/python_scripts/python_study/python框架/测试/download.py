#coding=utf-8
import os
from selenium import webdriver

fp=webdriver.ChromeFile()
fp.set_preference("browser.dowload.folderlist",2)
fp.set_preference("browser.dowload.manager.showWhenStarting",False)
fp.set_preference("browser.dowload.dir",os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")	                         #application/octet-stream 为内容的类型。
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-2").click()
# browser.download.dir 用于指定你所下载文件的目录。
# os.getcwd() 该函数不需要传递参数，用于返回当前的目录。
