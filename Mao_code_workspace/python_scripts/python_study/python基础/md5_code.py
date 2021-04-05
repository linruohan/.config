# -*- coding: utf-8 -*-
# 注册和登录代码：

"""
#需求：根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5，实现用户登录的验证
#用到的类和函数：
    类： User(object)：用户注册类
    函数：get_md5(s)：返回md5后的字符串
         login(username, password)：用户登录检测函数

"""
import hashlib, random

def get_md5(s):
    """
    #md5加密密码
    :param s:密码
    :return: 返回md5后的字符串
    """
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class UserRegistered(object):
    """
    #用户注册类：获取用户注册信息给密码加上登录名和“盐”
    #随机生成“盐”，并且将其保存在db_salt
    #给用户注册输入的密码加盐,并保存在db中
    #函数：
        __init__(self, username, password):获取注册信息，调用函数：userReg()
        userReg()：检查注册用户名是否以存在，存在返回：'Username has already been registered!'，
                    不存在返回：'Reg ok'，调用userSalt()
        userSalt():随机生成“盐”，并且将用户名和密码加盐保存
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def userReg(self):
        """
        #检查注册用户名是否以存在
        :return: 用户名不存在数据库。输出ok,存在输出:Username has already been registered!
        """
        if self.username not in db:
            self.userSalt()
            print(db)
            return 'Reg ok'

        else:
            return 'Username has already been registered!'

    def userSalt(self):
        """
        #随机生成“盐”，并且将用户名和密码加盐保存
        :return: 无
        """
        salt=''.join(chr(random.randint(48,122)) for i in range(20))
        db_salt[self.username]=salt
        db[self.username]=get_md5(self.username+self.password+db_salt[self.username])


class UserLogin(object):
    """
    #用户登录类，检查用户登录，返回登录成功或失败以及失败的原因
    #函数：__init__(self,username,password):拿取用户登录信息，调用userLogin()
         userLogin()：检查注册用户名是否以存在,若存在则检查输入密码是否和数据库中对应。
                        用户名不存在数据库。输出'Please register first!',存在且匹配输出:'Success!'
    """
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.userLogin()

    def userLogin(self):
        """
        #检查注册用户名是否以存在,若存在则检查输入密码是否和数据库中对应。

        :return: 用户名不存在数据库。输出'Please register first!',
                存在且匹配输出:'Success!'
        """
        if self.username not in db:
            return 'Please register first!'
        else:
            if db[self.username]==get_md5(self.username+self.password+db_salt[self.username]):
                return 'Success!'
            else:
                return 'Please cheack again!'


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#数据库
db = {}   #保存注册信息
db_salt={}#保存用户名对应的随机加密值
# 单元测试代码：
