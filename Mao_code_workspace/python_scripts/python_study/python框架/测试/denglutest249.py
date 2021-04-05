#coding=utf-8
'''
Created on 2017-7-25
@author: xiaohan
'''
from selenium import webdriver #引入selenium模块。
from selenium.webdriver.common.keys import Keys #模拟键盘输入。
import random,time #经常要用到，一个是产生随机数，一个是时间操作的功能
import unittest

class DengluTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome() #启动chrome浏览器
        self.browser.implicitly_wait(30) #隐性等待时间为30秒
        self.browser.maximize_window() #浏览器窗口最大化
        self.home_url='http://193.169.100.249:8087/itmsxianyang'
        self.username='admin'
        self.passwd='admin'
    ''' 定义登录函数'''
    def test_uselogin(self):
        browser=self.browser
        username=self.username
        passwd=self.passwd
        browser.get(self.home_url+'/')
        '''find elements'''
        e_user=browser.find_element_by_id("username")
        e_pwd=browser.find_element_by_id("password")
        e_user.clear()
        e_pwd.clear()
        e_user.send_keys(username)  #输入账号
        e_pwd.send_keys(passwd)    #输入密码
        time.sleep(1)
        e_pwd.send_keys(Keys.ENTER)#回车提交
        time.sleep(int(random.uniform(1, 10)))#随机产生一个1到9秒的随机整数，然后等待这个时间
    def tearDown(self):
        self.browser.quit() #退出浏览器
if __name__ == "__main__":
    unittest.main()
