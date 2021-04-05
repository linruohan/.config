#coding=utf-8
from unittest import *
import unittest
import unittest,time,re,sys,io,string
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class MyTestCase(unittest.TestCase):
    def __init__(self,*args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)

    def equal(self, first, second, msg=None):
        # self._write_to_log()
        super(MyTestCase, self).assertEqual(first, second, msg)

    def m12(self):
        a='123'
        b='22'
        self.equal((int(a)+1),int(b),u'添加卡口设备失败！')
s=MyTestCase()
# s.equal(12,1,'asd')
s.m12()
