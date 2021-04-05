#coding=utf-8
from itmsv1_mvc.common.basePage import Page

class Home_page(Page):
	# //本例使用XPath方式来进行定位，使用ID、name等方式均可定位
    '''操作元素如下所示：'''
    # 基础模块
    Basic_module='xpath=>//*[@id="menu_130402081930284387431bd38d30c4ac"]/p/a'
    # 卡口系统
    cross_system='xpath=>//*[@id="menu_1304261304150253833622fa401af96b"]/p/a'
    # 违法系统
    vio_system='xpath=>//*[@id="menu_130619095023993fa6f0e33461840c4b"]/p/a'
    # 布控系统
    Monitor_system='xpath=>//*[@id="menu_1305030918504367a63fdc4d5033ea81"]/p/a'
    # GPS系统
    GPS_system='xpath=>//*[@id="menu_130711115821246a8d2ec5fa025cf78c"]/p/a'
    # 短信平台
    SMS_platform='xpath=>//*[@id="menu_1305211608157961944e4b8ee198113e"]/p/a'
    # 流量分析
    Traffic_analysis='xpath=>//*[@id="menu_1305030838361678927dc9e50f2767b3"]/p/a'
    # 视频管理
    Video_management='xpath=>//*[@id="menu_13080709290681228edef50e3108843e"]/p/a'
    # 应急指挥
    Emergency_command='xpath=>//*[@id="menu_130716164458319caba6aa33d3d78bc7"]/p/a'
    # 信号控制
    Signal_control='xpath=>//*[@id="menu_130806084811984481e6bc0ae7979a84"]/p/a'
    # 停车诱导
    Parking_guidance='xpath=>//*[@id="menu_130806161937625499ae3241745dc757"]/p/a'
    # 交通设施
    Traffic_facilities='xpath=>//*[@id="menu_1310211154453754aa80667f3b44173d"]/p/a'
    # 道路挖占
    road_digging='xpath=>//*[@id="menu_13102113525445309b6551b1c005120c"]/p/a'
    # 勤务系统
    service_system='xpath=>//*[@id="menu_1310251126180903b934590cbc5290e3"]/p/a'
    # LED发布
    LED_release='xpath=>//*[@id="menu_131029102508828e9fb1368f49a3df53"]/p/a'
    # 地图管理
    map_manage='xpath=>//*[@id="menu_130613092559383983b85a84923d428d"]/p/a'
    # 通行证管理
    passes_manage='xpath=>//*[@id="menu_131202153958236e9e2ce62b00c9f113"]/p/a'
    # 事故分析
    Accident_analysis='xpath=>//*[@id="menu_1312171401175469a9c24efc6eda16fe"]/p/a'
    # 运维中心
    Operations_center='xpath=>//*[@id="menu_1408220902505154a56cd7094dac5bd9"]/p/a'
    # 信息交互
    Information_interaction='xpath=>//*[@id="menu_1312161602376024862822f94df79d57"]/p/a'
    # 决策分析
    Decision_analysis='xpath=>//*[@id="menu_1312171517265786bb594992c2e2961c"]/p/a'

    def basic(self):
        self.click(self.Basic_module)
    def cross(self):
        self.click(self.cross_system)
    def vio(self):
        self.click(self.vio_system)
    def monitor(self):
        self.click(self.Monitor_system)
    def gps(self):
        self.click(self.GPS_system)
    def sms(self):
        self.click(self.SMS_platform)
    def flow_anaysys(self):
        self.click(self.Traffic_analysis)
    def video(self):
        self.click(self.Video_management)
    def emergency(self):
        self.click(self.Emergency_command)
    def signal(self):
        self.click(self.Signal_control)
    def parking(self):
        self.click(self.Parking_guidance)
    def traffic(self):
        self.click(self.Traffic_facilities)
    def road_digging(self):
        self.click(self.road_digging)
    def sercice(self):
        self.click(self.service_system)
    def led(self):
        self.click(self.LED_release)
    def map(self):
        self.click(self.map_manage)
    def passes(self):
        self.click(self.passes_manage)
    def accident(self):
        self.click(self.Accident_analysis)
    def operate(self):
        self.click(self.Operations_center)
    def information(self):
        self.click(self.Information_interaction)
    def decision(self):
        self.click(self.Decision_analysis)
