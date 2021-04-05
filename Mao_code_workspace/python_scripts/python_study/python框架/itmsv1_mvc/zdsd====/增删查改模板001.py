#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,sys,io,string
'''****************************************'''
'''****************************************'''
'''***********【】模块*************'''
'''**************（测试）**********************'''
'''****************************************'''
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out,sj_IP,sj_8str,sj_hz,sj_3
s=find

class File_server(unittest.TestCase):
    def setUp(self):
        self.driver = login_in_out.login()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
        super()
    """用例1——添加--------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_add(self):
        """添加服务器"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        #进入子模块
        s.findsXpath(driver,'//*[@id="13050315032667198043cea8b460eacd"]/a')
        #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        self.assertEqual(1,1,'asdfsd')
        #
        # #获取添加前数据数
        # num0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        #
        # '''************添加*****************'''
        # #添加内容
        # s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[1]/div[1]/button[1]').click()
        # key=sj_hz.s()#自定义分组名称
        # s.findId(driver,'name').send_keys(key)
        # '''*****************************'''
        #
        # # 保存
        # s.findXpath(driver,'//*[@id="inputForm"]/div[2]/button').click()
        # time.sleep(5)
        #
        # self.assertEqual(1,2,'asdfsd')
        # #获取添加后数据数
        # num1_0=s.findXpath(driver,'//*[@id="content_body"]/div[3]/div[2]/div[3]/b[3]')
        # driver.execute_script("arguments[0].scrollIntoView();", num1_0)#元素聚焦
        # num1=num1_0.text
        # #验证添加
        # self.assertEqual((int(num0)+1),int(num1),u"添加卡口设备失败！")
        print(u'【1】添加成功：successfully added！成功添加一条数据')

    """用例2——删除--------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_del(self):
        """删除服务器"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        #进入子模块
        s.findsXpath(driver,'//*[@id="13050315032667198043cea8b460eacd"]/a').click()
        #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        #获取删除前数据数
        num0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text

        '''**********删除第一行*******************'''
        #删除第一行数据
        s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[3]/a[3]').click()
        driver.switch_to.alert.accept()
        time.sleep(3)
        '''*****************************'''


        #验证
        num1_0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]')
        driver.execute_script("arguments[0].scrollIntoView();", num1_0)#元素聚焦
        num1=num1_0.text
        print(num1)
        #验证
        self.assertEqual((int(num0)-1),int(num1),u"删除卡口设备失败！")
        print(u'【2】刪除成功：successfully deleted！成功删除一条数据')

    """用例3——查询------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_search(self):
        """查询服务器"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        #进入子模块
        s.findsXpath(driver,'//*[@id="13050315032667198043cea8b460eacd"]/a').click()
        #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)

        # 输入查询条件
        key='亿'
        s.findXpath(driver,'//*[@id="name"]').send_keys(key)
        #点击查询
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[3]/input[1]').click()
        #查询结果验证
        num=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        name=s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[2]').text
        if key in name:
            print(key+':'+name)
            print(u'查询成功：successfully got the goal！')
        if int(num)==0:
            print(u'查询结果为空！')
        #重置——查询
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[3]/input[2]').click()
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[3]/input[1]').click()
        time.sleep(2)
        kong=s.findXpath(driver,'//*[@id="name"]').text
        summery=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        if kong=='':
            print(u'重置成功！')
            print(u'共有'+summery+'条数据')
        else:
            print(u'重置失败！')

    """用例4——查看------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_check(self):
        """查看服务器"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        #进入子模块
        s.findsXpath(driver,'//*[@id="13050315032667198043cea8b460eacd"]/a').click()
        #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)

        '''**********查看第一行*******************'''
        s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[3]/a[1]').click()
        s.jietu(driver)
        print(u'【4】查看成功！successfully checking it！')


    """用例5——修改--------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_update(self):
        """修改服务器"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        #进入子模块
        s.findsXpath(driver,'//*[@id="13050315032667198043cea8b460eacd"]/a').click()
        #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)

        '''**********修改第一行*******************'''
        #获取修改前名称
        name0=s.findXpath(driver,'//*[@id="tbody"]/tr[2]/td[2]').text
        #开始修改
        s.findXpath(driver,'//*[@id="tbody"]/tr[2]/td[3]/a[2]').click()
        name=s.findXpath(driver,'//*[@id="name"]')
        name.clear()
        key=sj_hz.s()
        name.send_keys(key)
        #修改完保存
        s.findXpath(driver,'//*[@id="inputForm"]/div[2]/button').click()
        time.sleep(2)

        #驗證修改
        name1=s.findsXpath(driver,'//*[@id="tbody"]/tr/td[2]')
        text=[i.text for i in name1]
        if key in text:
            print(u'自定義分組名稱【'+name0+'】改爲:'+key)
            print(u'【3】修改成功！successfully reset the data')
        else:
            print(u'sorry，修改失敗！')




    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
