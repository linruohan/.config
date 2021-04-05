# coding=utf-8
from selenium import webdriver


class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根据browser_type的值去，控制启动不同的浏览器，这里主要是IE，Firefox, Chrome

    """
    def __init__(self, driver):
        self.driver = driver

    browser_type = "Firefox"   # maybe Firefox, Chrome, IE

    def get_browser(self):
        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
        :return: driver
        """

        if self.browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif self.browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif self.browser_type == 'IE':
            driver = webdriver.Ie()
        else: driver = webdriver.Chrome()

        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver
