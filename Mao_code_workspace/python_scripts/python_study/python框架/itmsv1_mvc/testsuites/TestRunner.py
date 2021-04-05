# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
import sys,time,io
sys.path.append('E:\\atom\\itmsv1_mvc\\common')
from mylog import Log as log
log=log()

path = 'E:\\atom\\itmsv1_mvc\\test_cases'

def creatsuitel():
    testunit=unittest.TestSuite()
    #discover 方法定义
    discover=unittest.defaultTestLoader.discover(path,pattern ='*.py',top_level_dir=path)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    log.info('discover:======> %s' % discover._tests)
    log.info('testunit:======> %s' % testunit)

    return testunit

if __name__ == "__main__":
    alltestnames = creatsuitel()
    now = time.strftime(' %Y-%m-%d-%H_%M_%S ',time.localtime(time.time()))
    filename = 'E:\\atom\\itmsv1_mvc\\test_report\\'+now+'result.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况：')
    #执行测试用例
    runner.run(alltestnames)
