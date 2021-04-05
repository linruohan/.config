# -*- coding: utf-8 -*-
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1
# 测试:

# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
lisa1 = Student('1Bart')
print('Students:', Student.count)
lisa2 = Student('2Bart')
print('Students:', Student.count)
lisa3 = Student('3Bart')
print('Students:', Student.count)
lisa4 = Student('1Bart')
print('Students:', Student.count)
lisa5 = Student('2Bart')
print('Students:', Student.count)
lisa6 = Student('3Bart')
print('Students:', Student.count)
