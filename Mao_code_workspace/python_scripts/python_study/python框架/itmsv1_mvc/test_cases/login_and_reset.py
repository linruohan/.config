# coding=utf-8
import sys,time
import unittest
sys.path.append('E:\\atom\\itmsv1_mvc\\page')
sys.path.append('E:\\atom\\itmsv1_mvc\\common')
from login_page import Login_page as page
from browser_engine import BrowserEngine
from mylog import Log as log
log=log()

class Login(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
    #重置
    @unittest.skip('暂时跳过此用例的测试')
    def test_reset_login(self):
        '''登录页面的重置功能'''
        homepage = page(self.driver)
        homepage.type_user('admin')
        homepage.type_passwd('admin')
        homepage.reset()#重置
        user=homepage.get_user_input()
        log.info('the user inputbox content is:%s' % user)
        passwd=homepage.get_passwd_input()
        log.info('the password inputbox content is:%s' % passwd)
        try:
            self.assertEqual(('',''),(user,passwd),u'reset failed!!!!!!')
            homepage.get_windows_img()
            log.info('*'*50)
            log.info('Test [[[[[ test_reset_login ]]]]] Pass.')
        except Exception as e:
            raise

    # 登录
    # @unittest.skip('暂时跳过此用例的测试')
    def test_nomal_login(self):
        '''正常登录功能'''
        homepage = page(self.driver)
        homepage.login('admin','admin')
        # homepage.type_user('admin')  # 调用页面对象中的方法
        # time.sleep(1)
        # homepage.type_passwd('admin')  # 调用页面对象中的方法
        # time.sleep(1)
        # homepage.click_submit_btn()
        # time.sleep(3)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            time.sleep(2)
            assert u'超级管理员' in homepage.get_login_name()  # 调用页面对象继承基类中的获取元素文本方法
            log.info('*'*50)
            log.info('Test [[[[[ test_nomal_login ]]]]] Pass.')
        except ValueError:pass
        except Exception as e:
            log.warning('Test failed.')
        return homepage
    # 退出登录
    # @unittest.skip('暂时跳过此用例的测试')
    def test_nomal_logout(self):
        '''正常退出功能'''
        homepage = self.test_nomal_login()
        # homepage.login('admin','admin')
        homepage.logout()
        try:
            time.sleep(2)
            assert '' in homepage.get_user_input()  # 调用页面对象继承基类中的获取元素文本方法
            log.info('*'*50)
            log.info('Test [[[[[ test_nomal_logout ]]]]] Pass.')
        except ValueError:pass
        except Exception as e:
            log.warning('Test failed.')

    def tearDown(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.close()
        # cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
