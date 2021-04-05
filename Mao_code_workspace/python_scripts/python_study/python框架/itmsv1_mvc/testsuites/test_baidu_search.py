# coding=utf-8
from selenium import webdriver
import sys,io,time
import unittest
sys.path.append('E:\\atom\\itmsv1_mvc\\element')
from baidu_homepage import HomePage as page
import sys,io
sys.path.append('E:\\atom\\itmsv1_mvc\\common')
from browser_engine import BrowserEngine
from mylog import Log as log
log=log()

class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    @classmethod
    def tearDownClass(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.close()
        # self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage = page(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()     #调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except ValueError :pass
        except Exception as e:
            print ('Test Fail.')

    def test_search2(self):
        homepage = page(self.driver)
        homepage.type_search('python')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法

if __name__ == '__main__':
    unittest.main()
