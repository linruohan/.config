#coding=utf-8
from itmsv1_mvc.common.basePage import Page

class Cross_main(Page):
    # //本例使用XPath方式来进行定位，使用ID、name等方式均可定位
    '''操作元素如下所示：'''
    # 卡口系统首页
    cross_fist_page='xpath=>//*[@id="leftMenu"]/div[1]/a'

    # 设备管理
    device_manage='xpath=>//*[@id="sidemenu"]/a[1]/p'
    # 卡口设备//*[@id="130502094519328f815bc3af1d635903"]/a
    devices='xpath=>//*[@id="130502094519328f815bc3af1d635903"]/a'
    # 自定义分组
    custom_group='xpath=>//*[@id="1404161355392917afeff9583374f9a1"]/a'
    # 文件服务器
    file_system='xpath=>//*[@id="13050315032667198043cea8b460eacd"]/a'
    # 设备功能
    devices_function='xpath=>//*[@id="13050614093381218f13d4006428bc9e"]/a'
    # 设备状态
    devices_status='xpath=>//*[@id="1307261601351405acf514ba3ff39a63"]/a'

    # 实时监控
    Realtime_monitoring='xpath=>//*[@id="sidemenu"]/a[2]/p'
    # 卡口监控
    cross_monitoring='xpath=>//*[@id="130522101806609b98cbef7e13f02086"]/a'
    # 卡口报警
    cross_alarm='xpath=>//*[@id="130725115024000982265067fd6ee483"]/a[2]/p'
    # 报警颜色
    alarm_color='xpath=>//*[@id="131128083220030196117fcf823f3758"]/a[2]/p'

    # 数据查询
    data_search='xpath=>//*[@id="sidemenu"]/a[3]/p'
    # 通行车辆查询
    cross_car_search='xpath=>//*[@id="131120162537187b91202c6b3a1ee2b8"]/a'
    # 通行车辆导出
    export_search = 'xpath=>//*[@id="131120162613328a94495cb016fb42ea"]/a'
    # 卡口图库
    maps_cross = 'xpath=>//*[@id="131120162633859197ed010382bb9dd3"]/a'
    # 碰撞对比
    Collision_contrast = 'xpath=>//*[@id="131120162655890a80fa4195028cfcef"]/a'
    # 卡口查询HBASE
    Hbase_search = 'xpath=>//*[@id="1409100830561719b16389e4f02b56ac"]/a'

    # 轨迹分析
    Path_analysis='xpath=>//*[@id="sidemenu"]/a[4]/p'

    # 套牌嫌疑分析
    double_analysis='xpath=>//*[@id="14012016292959349d01de33b7e015ea"]/a'
    # 跟踪徘徊分析
    follow_analysis='xpath=>//*[@id="140120163040625abe410511aefa7436"]/a'

    # 卡口统计
    Bayonet_statistics='xpath=>//*[@id="sidemenu"]/a[5]/p'
    # 卡口流量统计
    cross_flow_statistics='xpath=>//*[@id="13090915013605178936e57ebc02a839"]/a'
    # 高峰流量统计
    high_flow_statistics = 'xpath=>//*[@id="140220113301613598729f29e94cdc46"]/a'
    # 时段流量统计
    time_flow_statistics = 'xpath=>//*[@id="1403261002407941b92eb177c48719ce"]/a'
    # 颜色流量统计
    color_flow_statistics = 'xpath=>//*[@id="1403051602490698a9d9fe40be258449"]/a'
    # 区域流量统计
    area_flow_statistics = 'xpath=>//*[@id="1403181016463371be396272ee6ec0f6"]/a'
    # 平均速度统计
    average_speed_statistics = 'xpath=>//*[@id="1309091501570843a764ad4848743b44"]/a'
    # 外地车辆统计
    nonlocal_car_statistics = 'xpath=>//*[@id="13090915023316129a2ec30f59ccb459"]/a'
    # 道路流量统计
    road_flow_statistics = 'xpath=>//*[@id="1407021156296405b8ab2079952b4766"]/a'
    # 环比流量统计
    compare_flow_statistics = 'xpath=>//*[@id="1409021518048805ab748a90f31d9601"]/a'
    # 环比速度统计
    compare_speed_statistics = 'xpath=>//*[@id="140902151838850388d4bb8146f2c139"]/a'


    def first_page(self):
        self.click(self.cross_fist_page)
    def cross_devices(self):
        self.click(self.devices)
    def custom_groups(self):
        self.click(self.custom_group)
    def file_systems(self):
        self.click(self.file_system)
    def devices_functions(self):
        self.click(self.devices_function)
    def devices_statuss(self):
        self.click(self.devices_status)
    def Realtime_monitorings(self):
        self.click(self.Realtime_monitoring)
    def cross_monitorings(self):
        self.click(self.cross_monitoring)
    def cross_alarms(self):
        self.click(self.cross_alarm)
    def alarm_colors(self):
        self.click(self.alarm_color)
    def data_searchs(self):
        self.click(self.data_search)
    def cross_car_searchs(self):
        self.click(self.cross_car_search)
    def export_searchs(self):
        self.click(self.export_search)
    def maps_crosss(self):
        self.click(self.maps_cross)
    def Collision_contrasts(self):
        self.click(self.Collision_contrast)
    def Hbase_searchs(self):
        self.click(self.Hbase_search)
    def Path_analysiss(self):
        self.click(self.Path_analysis)
    def double_analysiss(self):
        self.click(self.double_analysis)
    def follow_analysiss(self):
        self.click(self.follow_analysis)
    def Bayonet_statisticss(self):
        self.click(self.Bayonet_statistics)
    def cross_flow_statisticss(self):
        self.click(self.cross_flow_statistics)
    def high_flow_statisticss(self):
        self.click(self.high_flow_statistics)
    def time_flow_statisticss(self):
        self.click(self.time_flow_statistics)
    def color_flow_statisticss(self):
        self.click(self.color_flow_statistics)
    def area_flow_statisticss(self):
        self.click(self.area_flow_statistics)
    def average_speed_statisticss(self):
        self.click(self.average_speed_statistics)
    def nonlocal_car_statisticss(self):
        self.click(self.nonlocal_car_statistics)
    def road_flow_statisticss(self):
        self.click(self.road_flow_statistics)
    def compare_flow_statisticss(self):
        self.click(self.compare_flow_statistics)
    def compare_speed_statisticss(self):
        self.click(self.compare_speed_statistics)
