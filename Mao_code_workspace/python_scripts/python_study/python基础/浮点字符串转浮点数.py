# -*- coding: utf-8 -*-
from functools import reduce

# def normal(name):
#     return name.capitalize()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normal, L1))
# print(L2)
#
#
# def prod(list):
#     return reduce(lambda x,y:x*y,list)
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')





def str2float(s):
    def char2num(s):
        digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7, '8': 8, '9': 9}
        return digits[s]
    def str2int(str):
        return reduce(lambda x,y:x*10+y,map(char2num,str))
    L,R=(s.split('.'))
    return str2int(L)+pow(10,-len(R))*str2int(R)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
