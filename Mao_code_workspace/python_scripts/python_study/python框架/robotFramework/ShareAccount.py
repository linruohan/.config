# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ShareAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://ip_addr/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_share_account(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("index_UTxt_UserName").clear()
        driver.find_element_by_id("index_UTxt_UserName").send_keys("username")
        driver.find_element_by_id("index_UTxt_Password").clear()
        driver.find_element_by_id("index_UTxt_Password").send_keys("password")
        driver.find_element_by_id("index_loginbutton").click()
        time.sleep(0.3)
        driver.get(self.base_url + "/student/shareCoupons.aspx")
        time.sleep(0.3)
        driver.find_element_by_css_selector("div.shareCoupons-button").click()
        time.sleep(0.3)
        #driver.find_element_by_id("you-nickname").clear()
        #driver.find_element_by_id("you-nickname").send_keys("")
        #使用退格键BACKSPACE
        driver.find_element_by_id("you-nickname").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("you-nickname").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("you-nickname").send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        data = driver.find_element_by_id("shareMassage").text
        time.sleep(1)
        print (data)
        driver.find_element_by_css_selector("input.get-Coupons-button").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()