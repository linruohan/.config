# coding=utf-8
from itmsv1_mvc.common.basePage import Page
from itmsv1_mvc.common.mylog import Log as log
import time
import unittest

log = log ()


class Device_status_page (Page,unittest.TestCase):
    # //本例使用XPath方式来进行定位，使用ID、name等方式均可定位
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''查询元素：---------content-frame'''
    # 设备名称
    dev_name = 'id=>s_name'
    # 设备编号
    dev_code = 'id=>s_code'