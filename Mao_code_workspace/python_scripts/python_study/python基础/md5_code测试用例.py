# -*- coding: utf-8 -*-
"""
测试md5加密的用户注册和登录功能
"""
import unittest
from unittest.test import suite

from md5_code import  UserRegistered,UserLogin
class TestUserRegistered(unittest.TestCase):

    def test_1_reg(self):
        #检查未注册数据返回
        for username,password in db_test_right.items():
            # print(username,':\t',password)
            self.assertEqual(UserRegistered(username,password).userReg(),'Reg ok')
        #检查已注册数据返回
        for username,password in db_test_false.items():
            # print(username,':\t',password)
            self.assertEqual(UserRegistered(username,password).userReg(), 'Username has already been registered!')
    def test_2_log(self):
        for username,password in db_test_right.items():
            # print(username,':\t',password)
            self.assertEqual(UserLogin(username,password).userLogin(),'Success!')
        #检查已注册数据返回
        for username,password in db_test_false.items():
            # print(username,':\t',password)
            self.assertEqual(UserLogin(username,password).userLogin(), 'Please cheack again!')


#-------------------------------------------------------
#-------------------------------------------------------

db_test_right = {'michael': '123456','bob': 'abc999','alice':'alice2008'}
db_test_false={'michael': '1234567','bob':'12 3456','alice':'Alice2008'}
if __name__ == '__main__':
    unittest.main()
