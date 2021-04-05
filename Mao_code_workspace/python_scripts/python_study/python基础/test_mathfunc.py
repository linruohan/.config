#coding=utf-8
import unittest
from mathfunc import *
class testMathFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2))
    def test_minus(self):
        self.assertEqual(1,minus(3,2))
    def test_multi(self):
        self.assertEqual(6,multi(2,3))
    def test_divide(self):
        self.assertEqual(2,divide(6,3))
        self.assertEqual(2.5,divide(5,2))
if __name__=='__main__':
    unittest.main(verbosity=2)
'''
在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果，
test_add (__main__.testMathFunc) ... ok
test_divide (__main__.testMathFunc) ... FAIL
test_minus (__main__.testMathFunc) ... ok
test_multi (__main__.testMathFunc) ... ok

======================================================================
FAIL: test_divide (__main__.testMathFunc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "F:\atom\mathtest\test_mathfunc.py", line 14, in test_divide
    self.assertEqual(2.5,divide(5,2))
AssertionError: 2.5 != 2

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)
'''
