#coding=utf-8
import unittest
#这里需要导入测试文件
import HTMLTestRunner
import time

import allcase_list
alltestnames=allcase_list.caselist()
testunit=unittest.TestSuite()
for testname in alltestnames:
    testunit.addTest(unittest.makeSuite(testname))
# #将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(baidu.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)

#取前面时间
now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))

#定义个报告存放路径，支持相对路径。
path = "D:\\"+now+r'result.html'
fp = open(path, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'百度搜索测试报告',
description=u'用例执行情况：')

#执行测试用例
runner.run(testunit)
