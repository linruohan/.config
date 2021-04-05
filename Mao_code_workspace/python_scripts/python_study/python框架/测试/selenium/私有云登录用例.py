#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import login #导入登录文件
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://passport.kuaibo.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        #私有云登录用例

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url +
        "/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")
        #调用登录模块
        login.login(self)
        #新功能引导
        driver.find_element_by_class_name("guide-ok-btn").click()
        time.sleep(3)
        #退出
        driver.find_element_by_class_name("Usertool").click()
        time.sleep(2)
        driver.find_element_by_link_text("退出").click()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
