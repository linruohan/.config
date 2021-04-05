# coding=utf-8
import  time
import unittest
from itmsv1_mvc.common.browser_engine import BrowserEngine
from itmsv1_mvc.common.mylog import Log as log
log = log()
from itmsv1_mvc.page.home_page import Home_page
from itmsv1_mvc.page.login_page import Login_page
from itmsv1_mvc.page.cross_system.cross_main import Cross_main
from itmsv1_mvc.page.cross_system.cross_device_page import Cross_device_page
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
        #进入卡口设备
        cls.cm.cross_devices()
        cls.s=Cross_device_page(cls.driver)
        time.sleep(2)

    @unittest.skip('暂时跳过此用例的测试')
    def test_000first(self):
        '''卡口首页'''
        # 首页截图
        self.pm.get_windows_img()
        time.sleep(1)

    # @unittest.skip('暂时跳过此用例的测试')
    def test_add(self):
        '''添加卡口设备'''
        self.s.selecting_road()#默认第三个道路信息
        num0=int(self.s.get_counts())
        self.s.adding()
        self.s.adds_org()
        self.s.adds_type('闯红灯')
        self.s.type_name('测试设备名称')
        self.s.type_brand('大华')
        self.s.adds_dev_func(['卡口检测','单点超速'])
        self.s.type_pattern(sj())
        self.s.go_env_setting()
        self.s.type_ip(sjip())
        self.s.type_timeout(60)
        # self.s.select_server()
        time.sleep(1)
        self.s.go_direction()
        self.s.car_direction()
        self.s.car_road('2')
        time.sleep(1)
        self.s.go_build_info()
        self.s.select_factory('西安翔迅')
        self.s.saving()
        num1=int(self.s.get_counts())
        assert num0+1==num1
        self.assertEqual(num0+1,num1)
        log.info('successfully added！设备添加成功！')

    # @unittest.skip('暂时跳过此用例的测试')
    def test_check(self):
        '''查看卡口设备'''
        key='测试设备名称'
        self.s.stype_device_name (key)
        self.s.searching ()
        num=self.s.get_counts()
        self.s.view(key)
        name=self.s.get_view_name()
        self.assertEqual(name,key)
        log.info('name 为【%s】的卡口设备信息查看successfullly！<<<'%key)
    # @unittest.skip('暂时跳过此用例的测试')
    def test_search(self):
        '''查询卡口设备'''
        key = '测试设备名称'
        self.s.stype_device_name (key)
        self.s.searching ()
        list=self.s.namelist()
        self.assertNotEqual(len([s for s in list if key in s]), 0)
        log.info('查询设备【%s】，确已存在！'%key)
    # @unittest.skip('暂时跳过此用例的测试')
    def test_update(self):
        '''修改卡口设备'''
        key = '测试设备名称'
        key2 = '修改后的'
        self.s.stype_device_name (key)
        self.s.searching ()
        self.s.update(key)
        self.s.type_update_name(key2)
        self.s.saving()
        # 测试是否修改
        # if self.s.compareUpdate(key,key2):
        #     log.info ('修改设备【%s】，现在已正确修改！' % key)
        if self.s.get_counts_key(key2)==1:
            log.info ('设备名称【%s】修改为【%s】，现在已正确修改！' % (key,key2))
    # @unittest.skip('暂时跳过此用例的测试')
    def test_xdelete(self):
        '''删除卡口设备'''
        key = '修改后的'
        self.s.stype_device_name (key)
        self.s.searching ()
        self.s.delete(key)
        if self.s.get_counts_key(key)==0:
            log.info ('设备名称为【%s】，现在已正确删除！' % key)
    def tearDown(cls):
        # cls.driver.close()
        cls.driver.quit()  # cls.driver.Dispose()


if __name__ == '__main__':
    unittest.main()
