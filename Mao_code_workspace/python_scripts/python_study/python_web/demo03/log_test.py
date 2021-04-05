#coding=utf-8
import time,sys,os,io
from selenium import webdriver
from log import Log
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

log = Log(logger='TestMyLog').getlog()
class TestMyLog(object):

    def print_log(self):
        driver = webdriver.Chrome()
        log.info(u"打开浏览器")
        driver.maximize_window()
        log.info(u"最大化浏览器窗口。")
        driver.implicitly_wait(8)

        driver.get("https://www.baidu.com")
        log.info(u"打开百度首页。")
        time.sleep(1)
        log.info(u"暂停一秒。")
        driver.quit()
        log.info(u"关闭并退出浏览器。")

testlog = TestMyLog()
testlog.print_log()
