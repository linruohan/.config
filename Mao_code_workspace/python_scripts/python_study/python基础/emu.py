# -*- coding: utf-8 -*-
from enum import Enum, unique
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender(0))
if bart.gender == Gender.Male:
    print('测试通过!')
    print(bart.gender)
else:
    print('测试失败!')
    print(bart.gender)
