#coding=utf-8
import unittest
from filename.py import classname

if __name__ == '__main__':
    '''建立测试集合并初始化'''
    suite=unittest.TestSuite()
    '''测试用例列表'''
    tests=[classname1(def),classname2(def)]
    '''将用例添加到测试集中'''
    suite.addTests(tests)
'''
# 直接用addTest方法添加单个TestCase
suite.addTest(TestMathFunc("test_multi"))

# 用addTests + TestLoader
# loadTestsFromName()，传入'模块名.TestCase名'
suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表

# loadTestsFromTestCase()，传入TestCase
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
'''
    '讲测试结果输出到report中去'
    with open(unittestTextReport.txt,'a') as f:
        '初始化测试框架驱动'
        runner=unittest.TextTestRunner(verbosity=2)
        '执行测试集，并输出测试结果'
        runner.run(suite)
