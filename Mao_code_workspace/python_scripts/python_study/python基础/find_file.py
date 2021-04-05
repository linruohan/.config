# -*- coding: utf-8 -*-
import os
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#=================
'''查询当前目录及子目录中包含特定字符串的文件，并输出其绝对路径'''
#=================

'''选择并输入主路径'''
pwd = 'E:\\atom'
'''输入要查询的字符串'''
searchstr='py'
print('Abspath                                                     Filename')
print('-'*100)
L0=[]
num=0
for root,dirs,files in os.walk(pwd):
    #找到文件中含有特定字符串的files的name，和根root路径进行拼接，形成绝对路径
    L1=[os.path.join(root, name) for name in files if name.find(searchstr) >=0]
    if len(L1) >0:
        print('\n【【【此路径下，文件个数为：',len(L1),'\n')
        L0.append(len(L1))
        for i in L1:
            abspath = i
            # print(i)
            print(abspath,'='*10,os.path.split(abspath)[1])
#文件个数统计
'''方法一'''
for i in L0:
    num+=i
'''方法二'''
from functools import reduce
def add(x, y):
    return x + y
num1=reduce(add,L0)
print('num1==',num1)


print('\n\n\n',u'合计，在%s及其子文件夹中，包含字符串%s的file文件个数为%s个。'%(pwd,searchstr,num))
print('\n\n\n',u'合计，在%s及其子文件夹中，包含字符串%s的file文件个数为%s个。'%(pwd,searchstr,num1))
