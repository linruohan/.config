# coding=utf-8
from itmsv1_mvc.common.basePage import Page
from itmsv1_mvc.common.mylog import Log as log
import time
import unittest

log = log ()


class Cross_device_page (Page,unittest.TestCase):
    # //本例使用XPath方式来进行定位，使用ID、name等方式均可定位
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''查询元素：---------content-frame'''
    # 设备名称
    dev_name = 'id=>s_name'
    # 设备编号
    dev_code = 'id=>s_code'
    # 建设厂家
    dev_factory = 'id=>dev-select'
    # 设备类型
    dev_type = 'id=>selXSF'
    type_dic = ['闯红灯', '公路卡口设备', '测速设备', '闭路电视', '移动摄像', '警务通', '区间测速', '卫星定位装置', '其它电子设备']
    # 设备功能
    device_function = 'id=>deviceTypeNames'
    kkjc = 'id=>dtTreeSpace_2_span'
    ''''''
    lljc = 'id=>dtTreeSpace_17_span'
    func_dict = {'2': '卡口检测', '3': '违法检测', '4': '单点超速', '5': '区间超速', '6': '应急车道', '7': '按车道限速', '8': '不按车道行驶',
                 '9': '违反信号灯', '10': '禁止左转掉头', '11': '违反禁止标线', '12': '不按导向行驶', '13': '违法停车', '14': '占用专用车道', '15': '逆行',
                 '16': '其他', '17': '流量检测'}
    # 所属部门
    device_org = 'id=>orgNames'
    device_org0 = 'id=>orgTreeSpace_1_span'  # 根目录
    device_org1 = 'id=>orgTreeSpace_2_span'  # 第一部门
    device_org2 = 'id=>orgTreeSpace_3_span'  # 第二部门
    # IP 地址
    ip = 'id=>s_ip'
    # 查询
    search = 'xpath=>//*[@id="content_body"]/div[4]/div[1]/form/table/tbody/tr[2]/td[8]/input[1]'
    # 重置
    reset = 'xpath=>//*[@id="content_body"]/div[4]/div[1]/form/table/tbody/tr[2]/td[8]/input[2]'

    '''批量操作元素：'''
    # 导出
    export = 'xpath=>//*[@id="exportXls"]'
    # 添加
    add = 'xpath=>//*[@id="addImg"]'
    # 删除
    delete = 'xpath=>//*[@id="delImg"]'

    # 道路信息
    roads_info = 'id=>tree-rec_1_span'
    # 城市主干道
    main_road = 'id=>tree-rec_2_span'
    # 其他道路
    other_road = 'id=>tree-rec_4_span'
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''单个操作元素-----myIframe'''
    # 全选
    all_select = 'id=>selectAll'
    # 单选
    single_select = 'xpath=>//*[@id="rowcount0"]/td[1]/input'
    # 查看
    see_dev = 'xpath=>//*[@id="rowcount0"]/td[9]/a[1]'
    see_dev_name_info = 'xpath=>//*[@id="content_body"]/div[2]/div[1]/table[1]/tbody/tr[1]/td[4]'
    # 修改
    update_dev = 'xpath=>//*[@id="rowcount0"]/td[9]/a[2]'
    # 删除
    delete_dev = 'xpath=>//*[@id="rowcount0"]/td[9]/a[3]'
    '''翻页和统计元素'''
    # 当前页
    current_page = 'xpath=>//*[@id="content_body"]/div/div/div[2]/b[1]'
    # 每页15条
    page_number = 'xpath=>//*[@id="content_body"]/div/div/div[2]'
    # 共多少页
    pages = 'xpath=>//*[@id="content_body"]/div/div/div[2]/b[2]'
    # 共多少条记录
    numbers = 'xpath=>//*[@id="content_body"]/div/div/div[2]/b[3]'
    # 首页
    first_one = 'xpath=>//*[@id="content_body"]/div/div/div[1]/ul/li[1]/a'
    # 尾页
    last = 'xpath=>//*[@id="content_body"]/div/div/div[1]/ul/li[5]/a'
    # 上翻
    back_page = 'xpath=>//*[@id="content_body"]/div/div/div[1]/ul/li[2]/a'
    # 下翻
    forward_page = 'xpath=>//*[@id="content_body"]/div/div/div[1]/ul/li[4]/a'
    # 第1页
    one = 'xpath=>//*[@id="content_body"]/div/div/div[1]/ul/li[3]/a'

    # ****************-添加  begin-----------------------
    # 基本信息
    basic_info = 'xpath=>//*[@id="inputForm"]/ul/li[1]/a'
    # 南阳路
    its_road = 'xpath=>/html/body/div[2]/div/form/div[1]/div[1]/div[1]/table/tr[1]/td[2]/input'
    # 所属部门
    add_org = 'xpath=>//*[@id="orgNames"]'
    # 所属部门编号
    org_id = 'id=>codeStart'
    # 设备类型
    add_dev_type = 'xpath=>//*[@id="tab1"]/div[1]/table/tbody/tr[3]/td[2]/div/button'
    # 设备类型编号
    dev_id = 'id=>codeMiddle'
    # 设备编号结束
    end_id = 'id=>codeEnd'
    # 设备名称
    name = 'xpath=>//*[@id="name"]'
    # 设备品牌
    dev_brand = 'xpath=>//*[@id="trademark"]'
    # deviceTypeNames设备功能
    deviceTypeNames = 'xpath=>//*[@id="deviceTypeNames"]'
    # 设备型号
    dev_pattern = 'xpath=>//*[@id="pattern"]'

    # 环境配置
    env_setting = 'xpath=>//*[@id="inputForm"]/ul/li[2]/a'
    add_ip = 'id=>ip'
    server = 'xpath=>//*[@id="ftpId_chzn"]/a/div/b'
    server1 = 'xpath=>//*[@id="ftpId_chzn"]/a/span'
    timeout = 'id=>timeout'
    dev_analysis = 'xpath=>//*[@id="tab2"]/div[1]/table/tbody/tr[5]/td[2]/ul/li[1]'
    dev_analysis_sel = 'id=>isblackanalyse1'
    center_anaysis = 'xpath=>//*[@id="tab2"]/div[1]/table/tbody/tr[5]/td[2]/ul/li[2]'
    center_anaysis_sel = 'id=>isblackanalyse2'

    # 方向配置
    direction_setting = 'xpath=>//*[@id="inputForm"]/ul/li[3]/a'
    e_w = 'id=>directionCode_01'
    w_e = 'id=>directionCode_02'
    s_n = 'id=>directionCode_03'
    n_s = 'id=>directionCode_04'
    car_road_num = 'xpath=>//*[@id="select01"]'
    limit_speed1 = 'id=>carlimitspeed_01'
    limit_speed2 = 'id=>carlimitspeed_02'
    limit_speed3 = 'id=>carlimitspeed_03'
    limit_speed4 = 'id=>carlimitspeed_04'

    # 建设信息
    select_build = 'xpath=>//*[@id="companyId"]'
    build_info = 'xpath=>//*[@id="inputForm"]/ul/li[4]/a'
    factory = 'xpath=>//*[@id="companyId_chzn"]/a/span'
    factory1 = 'id=>companyId_chzn_o_1'
    # 地图位置
    map_situation = 'xpath=>//*[@id="inputForm"]/ul/li[5]/a'
    # 监控配置
    monitor_setting = 'xpath=>//*[@id="inputForm"]/ul/li[6]/a'

    # ***************添加  end------------------------
    save_menu = 'xpath=>//*[@id="submit_btn"]'

    # %%%%%%%%%%%%%%%%%%------------查询开始---------%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def get_counts(self):
        '''获取记录条数'''
        self.switch_frame ('content-frame')
        self.switch_frame ('myIframe')
        s = self.get_text (self.numbers)
        self.switch_current_frame ()
        return s

    def stype_device_name(self, text):
        '''查询输入'''
        self.switch_frame ('content-frame')
        self.type (self.dev_name, text)
        self.switch_current_frame ()

    def stype_device_code(self, text):
        '''查询输入'''
        self.switch_frame ('content-frame')
        self.type (self.dev_code, text)
        self.switch_current_frame ()

    def stype_device_factory(self, text):
        '''查询输入'''
        self.switch_frame ('content-frame')
        self.select (self.dev_factory, text)
        self.switch_current_frame ()

    def stype_device_type(self, text):
        '''查询输入'''
        self.switch_frame ('content-frame')
        if text in self.type_dic:
            self.select (self.dev_type, text)
            log.info ('Enter device type :%s for searching.' % text)
        else:
            log.info ('device type has no such items:%s  .' % text)
        self.switch_current_frame ()

    def stype_dev_list_function(self, list1):
        '''查询输入'''
        self.switch_frame ('content-frame')
        self.click (self.device_function)
        if len (list1) and isinstance (list1, list):
            for i in list1:
                x = 'id=>dtTreeSpace_%s_span' % str (i)
                self.click (self.find_element (x))
        self.switch_current_frame ()

    def stype_dev_org(self):
        '''查询输入'''
        self.switch_frame ('content-frame')
        self.click (self.device_org)
        self.click (self.device_org1)
        self.switch_current_frame ()

    def stype_dev_ip(self, text):
        '''查询输入'''
        self.switch_frame ('content-frame')
        self.type (self.ip, text)
        self.switch_current_frame ()

    def searching(self):
        '''查询'''
        self.switch_frame ('content-frame')
        self.click (self.search)
        self.switch_current_frame ()

    def reseted(self):
        '''查询重置'''
        self.switch_frame ('content-frame')
        self.click (self.reset)
        self.switch_current_frame ()

    # %%%%%%%%%%%%%%%%%%------------查询结束---------%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # 批量操作按钮

    def exporting(self):
        '''导出'''
        self.switch_frame ('content-frame')
        self.click (self.export)
        self.switch_current_frame ()

    def adding(self):
        '''添加'''
        self.switch_frame ('content-frame')
        self.click (self.add)
        time.sleep (1)
        self.switch_frame ('myIframe')

    def deleting(self):
        '''删除'''
        self.switch_frame ('content-frame')
        self.click (self.delete)
        self.switch_current_frame ()

    def selecting_road(self):
        '''选择目标道路'''
        self.switch_frame ('content-frame')
        self.click (self.other_road)
        self.switch_current_frame ()

    # -------------以上属于content——frame-------------------
    # 选择道路，进行特定道路下设备的增删查改

    def get_rows_by_key(self, key):
        '''通过关键字查找行数'''
        self.switch_frame ('content-frame')
        self.switch_frame ('myIframe')
        kname = [kname.text for kname in self.find_elements ('xpath=>//tbody[@id="tbody"]/tr/td[2]')]
        kindex = [kname.index (i) for i in kname if key in i][0]
        return kindex

    def view(self, key):
        '''通过关键字进行查看'''
        n = self.get_rows_by_key (key)
        self.click ("xpath=>//*[@id='rowcount" + str (n) + "']/td[9]/a[1]")
        log.info (u'对 name 为[%s]的设备信息开始进行查看！>>>' % key)
        self.switch_current_frame ()

    def update(self, key):
        '''通过关键字进行修改'''
        n = self.get_rows_by_key (key)
        self.click ("xpath=>//*[@id='rowcount" + str (n) + "']/td[9]/a[2]")
        log.info (u'对 name 为[%s]的设备信息开始进行修改！>>>' % key)
        self.switch_current_frame ()
    def get_counts_key(self,key):
        self.stype_device_name (key)
        self.searching ()
        s1 = len ([s for s in self.namelist () if key in s])
        return s1
    def compareUpdate(self, key, key2):
        self.stype_device_name (key2)
        self.searching ()
        s1 = len ([s for s in self.namelist () if key2 in s])
        self.assertEqual (s1, 1)
        # self.stype_device_name (key)
        # self.searching ()
        # s2 = len ([s for s in self.namelist () if key in s])
        # self.assertEqual (s2, 0)
        return True

    def type_update_name(self, key):
        self.switch_frame ('content-frame')
        self.switch_frame ('myIframe')
        self.type_name (key)
        self.switch_current_frame ()

    def delete(self, key):
        '''通过关键字进行删除'''
        n = self.get_rows_by_key (key)
        self.click ("xpath=>//*[@id='rowcount" + str (n) + "']/td[9]/a[3]")
        self.switch_alert_accept ()
        log.info (u' name 为[%s]的设备信息已被删除！>>>' % key)
        self.switch_current_frame ()

    def namelist(self):
        '''第一页卡口设备名称列表'''
        self.switch_frame ('content-frame')
        self.switch_frame ('myIframe')
        kname = [kname.text for kname in self.find_elements ('xpath=>//tbody[@id="tbody"]/tr/td[2]')]
        self.switch_current_frame ()
        return kname

    def view_first_row(self):
        '''第一行查看'''
        self.switch_frame ('content-frame')
        self.switch_frame ('myIframe')
        self.click (self.see_dev)
        self.switch_current_frame ()

    def get_view_name(self):
        '''通过关键字查找，返回卡口设备的名称'''
        self.switch_frame ('content-frame')
        self.switch_frame ('myIframe')
        name = self.get_text (self.see_dev_name_info)
        self.switch_current_frame ()
        return name

    # 获取页面信息：第几页，多少页，多少条
    def page_messages(self):
        self.get_text (self.delete_dev)
        current_page_num = self.get_text (self.current_page)
        allpages = self.get_text (self.pages)
        numbers = self.get_text (self.numbers)
        page_number = self.get_text (self.page_number).split ('条')[0].split ('页')[-1]
        log.info ('current_page_num, allpages, numbers, page_number' + current_page_num, allpages, numbers, page_number)
        return current_page_num, allpages, numbers, page_number

    # **********************
    # ***********添加**基础信息*********************>>>>>>>>>>>>>
    # *******************
    # 选择组织机构
    def adds_org(self):
        # js = 'document.getElementById("orgNames").removeAttribute("readonly");'
        # self.js (js)
        self.click (self.add_org)
        time.sleep(1)
        self.click (self.device_org1)

    # 选择设备类型
    def adds_type(self, text):
        if text in self.type_dic:
            self.click (self.add_dev_type)
            num = self.type_dic.index (text) + 1
            type = 'xpath=>.//*[@id="dropdown-ul"]/li[%s]' % num
            self.click (type)
            log.info ('Enter device type :%s for searching.' % text)
        else:
            log.info ('device type has no such items:%s  .' % text)

    # 填写设备名称
    def type_name(self, text):
        self.clear_text (self.name)
        self.type (self.name, text)

    # 填写设备品牌
    def type_brand(self, text):
        self.type (self.dev_brand, text)

    # 添加功能
    def adds_dev_func(self, list1):
        time.sleep (1)
        dic = [v for k, v in self.func_dict.items ()]
        num = [dic.index (m) + 2 for m in dic for n in list1 if n == m]
        # print (dic, num[0])
        self.click (self.deviceTypeNames)
        time.sleep (1)
        for i in range (len (num)):
            path = 'xpath=>//*[@id="dtTreeSpace_%s_span"]' % num[i]
            self.click (path)
            log.info ('dev_function %s has been selected.' % list1[i])

    def type_pattern(self, text):
        self.type (self.dev_pattern, text)

    # **********************
    # ***********添加**环境配置信息*********************>>>>>>>>>>>>>
    # *******************
    def go_env_setting(self):
        self.click (self.env_setting)

    def type_ip(self, ip):
        self.type (self.add_ip, ip)

    def type_timeout(self, t):
        self.type (self.timeout, t)

    def select_server(self):
        self.click (self.server)
        time.sleep (1)
        self.click (self.server1)

    def anaysis_module(self, n):
        dev_analysis = self.get_text (self.dev_analysis)
        center_anaysis = self.get_text (self.center_anaysis)
        if n == 1:
            self.click (self.dev_analysis_sel)
        elif n == 2:
            self.click (self.center_anaysis_sel)

    # **********************
    # ***********方向配置*********************>>>>>>>>>>>>>
    # *******************
    def go_direction(self):
        self.click (self.direction_setting)

    def car_direction(self):
        self.click (self.e_w)

    def car_road(self, value):
        self.select_value (self.car_road_num, value)

    # **********************
    # ***********建设信息*********************>>>>>>>>>>>>>
    # *******************
    def go_build_info(self):
        self.click (self.build_info)

    def select_factory(self, text):
        # js='document.getElementById("companyId_chzn").innerHTML="<span>%s</span>";'%text
        # print(js)
        # self.js(js)
        time.sleep (1)
        self.click (self.factory)
        time.sleep (2)
        self.click (self.factory1)
        self.switch_current_frame ()
    # **********************
    # ***********地图位置*********************>>>>>>>>>>>>>
    # *******************
    def go_map(self):
        self.click (self.map_situation)

    def select_map_sit(self, text):
        mapx, mapy = text
        self.type (self.map_x, mapx)
        self.type (self.map_y, mapy)

    # **********************
    # ***********监控配置*********************>>>>>>>>>>>>>
    # *******************
    def go_monitor_setting(self):
        self.click (self.monitor_setting)

    def saving(self):
        self.switch_frame ('content-frame')
        self.switch_frame ('myIframe')
        e1 = self.find_element (self.save_menu)
        self.js_to_view ("arguments[0].scrollIntoView();", e1)  # 元素聚焦
        e1.click ()
        time.sleep (1)
        self.switch_current_frame ()
