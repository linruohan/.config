# -*- coding:utf-8 -*-
try:
    import configparser
except:
    from six.moves import configparser
import os.path
from selenium import webdriver
from itmsv1_mvc.common.mylog import Log as log
log=log()



class BrowserEngine(object):

    dir = os.path.dirname(os.path.dirname(__file__))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/driver/chromedriver.exe'
    ie_driver_path = dir + '/driver/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.dirname(__file__)) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        log.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        log.info("The test server url is: %s" % url)


        if browser == "Firefox":
            driver = webdriver.Firefox()
            log.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            log.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            log.info("Starting IE browser.")

        driver.get(url)
        log.info("Open url: %s" % url)
        driver.maximize_window()
        log.info("Maximize the current window.")
        driver.implicitly_wait(10)
        log.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        log.info("Now, Close and quit the browser.")
        self.driver.quit()

if __name__ == '__main__':
    # browser=BrowserEngine()
    config = configparser.ConfigParser()
    # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
    file_path = os.path.dirname(os.path.dirname(__file__)) + '/config/config.ini'
    config.read(file_path)

    browser = config.get("browserType", "browserName")
    log.info("You had select %s browser." % browser)
    url = config.get("testServer", "URL")
    log.info("The test server url is: %s" % url)
