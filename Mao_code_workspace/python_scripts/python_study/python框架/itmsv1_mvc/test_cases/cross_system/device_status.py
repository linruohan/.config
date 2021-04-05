# coding=utf-8
import  time
import unittest
from itmsv1_mvc.common.browser_engine import BrowserEngine
from itmsv1_mvc.common.mylog import Log as log
log = log()
from itmsv1_mvc.page.home_page import Home_page
from itmsv1_mvc.page.login_page import Login_page
from itmsv1_mvc.page.cross_system.cross_main import Cross_main
from itmsv1_mvc.page.cross_system.device_status_page import Device_status_page
from itmsv1_mvc.common.sj_12str import sj
from itmsv1_mvc.common.sj_IP import sjip
class Cross(unittest.TestCase):
    @classmethod
    def setUp(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        cls.pl = Login_page(cls.driver)
        cls.pl.login('admin', 'admin')
        cls.pm = Home_page(cls.driver)
        # 进入卡口系统
        cls.pm.cross()
        time.sleep(2)
        '''以下代码只有第一条首页截图时注释'''
        cls.cm=Cross_main(cls.driver)
        #进入设备状态
        cls.cm.devices_statuss()
        cls.s=Device_status_page(cls.driver)
        time.sleep(2)



    # @unittest.skip('暂时跳过此用例的测试')
    def test_search(self):
        '''查询卡口设备'''
        page = self.s.get_source ()
        with open ('卡口设备状态.html', 'w',encoding='utf-8')as f:
            f.write (page)
        self.s.get_windows_img()

    def tearDown(cls):
        pass
        # cls.driver.close()
        cls.driver.quit()  # cls.driver.Dispose()


if __name__ == '__main__':
    unittest.main()
