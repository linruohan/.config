# -*- coding: utf-8 -*-
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class Screen(object):
    def __init__(self):
        self.__width=0
        self.__height=0
        self.__resolution=0

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError("must be int")
        self.__width=value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError("must be int")
        self.__height=value

    @property
    def resolution(self):
        return self.__width*self.__height




# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print(u'测试通过!')
else:
    print(u'测试失败!')
