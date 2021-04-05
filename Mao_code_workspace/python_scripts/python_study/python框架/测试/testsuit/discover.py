#coding=utf-8
import unittest
import os,sys
import time,HTMLTestRunner

url=r'D:/Python/testsuit/test_case'

def createsuitel():
    testunit=unittest.TestSuite()
    #discover difined
    discover=unittest.defaultTestLoader.discover(url,
    pattern ='test_*.py',
    top_level_dir=None)
    #discover method selected test_case,loop to add TestSuite
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print (testunit)
    return testunit

alltestnames=createsuitel()
now=time.strftime('%Y-%m-%M-%H %M %S',time.localtime(time.time()))
filename='D:\\'+now+'result.html'
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'测试用例集合测试报告',
description=u'用例执行情况如下所示：'
)

#执行测试用例
runner.run(alltestnames)
