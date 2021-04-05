# -*- coding: utf-8 -*-
from enum import Enum, unique
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# 类型=type，returntype===Gender中的男女，字符串
def type_limit(*typeLimit,**returnType):
    def test_value_type(func):
        def wrapper(self,*param,**kw):

            '''个数'''
            length = len(typeLimit)#限制类型有几个
            if length != len(param):#student有几个参数
                raise ValueError("The list of typeLimit and param must have the same length")

            '''类型'''
            for index in range(length):
                t = typeLimit[index]#str， Gender
                p = param[index]    #name，gender
                if not isinstance(p,t):#
                    raise ValueError("The param %s should be %s,but it's %s now!"%(str(p),type(t),type(p)))

            '''返回值类型'''
            res = func(self,*param,**kw)
            if "returnType" in returnType:
                #  Male = 0
                # Female = 1
                limit = returnType["returnType"]
                if  not isinstance(res,limit):
                    raise ValueError("This function must return a value that is %s,but now it's %s"%(limit,type(res) ) )
            return res
        return wrapper
    return test_value_type

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    @type_limit(str,Gender)
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

# 测试:
bart = Student('Bart',Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
