#coding=utf-8
import unittest
from test_mathfunc import testMathFunc

if __name__ == '__main__':
    suite=unittest.TestSuite()

    # tests=[testMathFunc("test_add"),testMathFunc("test_minus"),testMathFunc("test_multi"),testMathFunc("test_divide")]
    #
    # # 直接用addTest方法添加单个TestCase
    suite.addTest(testMathFunc("test_multi"))
    #
    # # 用addTests + TestLoader
    # # loadTestsFromName()，传入'模块名.TestCase名'
    # suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    # suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表
    #
    # # loadTestsFromTestCase()，传入TestCase
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    suite.addTests(suite)
    with open('math/report.txt','a') as f:
        runner=unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)
