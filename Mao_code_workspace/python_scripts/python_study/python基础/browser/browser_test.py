# coding=utf-8
import time
from browser_engine import BrowserEngine


class TestBrowserEngine(object):

    def open_browser(self):
        browserengine = BrowserEngine(self)
        driver = browserengine.get_browser()


tbe = TestBrowserEngine()
tbe.open_browser()
