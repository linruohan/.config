# -*- coding: utf-8 -*-
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,s):
        if isinstance(s,str) and s:
            self.__gender = s
        else:
            raise ValueError('bad score')
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败001!')
else:
    print('测试成功001!')
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败002!')
    else:
        print('测试成功002!')
