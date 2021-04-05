#coding=utf-8
import unittest
import HTMLTestRunner
import os,time

url='D:\\Python\\testsuit\\test_case'

def createSuite():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(url,pattern='test_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    print(testunit)
    return testunit

alltestnames=createSuite()
now=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
filename='D:\\Python\\testsuit\\report\\'+now+'result.html'
fp=open(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'测试报告',
    description=u'用例执行情况',
)
runner.run(alltestnames)
#########控制什么时间执行用例
k=1
while k<2:
    timing=time.strftime('%H_%M',time.localtime(time.time()))
    if timing=='10_56':
        print(u'开始运行脚本')
        runner.run(alltestnames)
        print(u'运行结束退出')
        break
    else:
        time.sleep(3)
        print(timing)
