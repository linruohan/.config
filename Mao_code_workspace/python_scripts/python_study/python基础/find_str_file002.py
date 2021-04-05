# -*- coding: utf-8 -*-
import os
import sys,io
from functools import reduce
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#=================
'''查询当前目录及子目录中包含特定字符串的文件，并输出其绝对路径'''
#=================

class find_file(object):
    def __init__(self,path,str1):
        self.path=path
        self.str1=str1
        print('Abspath                                                     Filename')
        print('-'*100)

    def add_01(self,x, y):
        return x + y

    def dir_001(self):
        path=self.path
        str1=self.str1
        print('dir=========全路径                                        Filename')
        dir_num=[]
        for root,dirs,files in os.walk(path):
            #找到文件中含有特定字符串的files的name，和根root路径进行拼接，形成绝对路径
            dir_L1=[os.path.join(root, name) for name in dirs if name.find(str1) >=0]
            if len(dir_L1) >0:
                print('本次dir有%s个'%len(dir_L1))
                dir_num.append(len(dir_L1))
                for i in dir_L1:
                    abspath1 = i
                    print(abspath1,'='*10,os.path.split(abspath1)[1])
        dir_num0=reduce(self.add_01,dir_num)
        dir_num0_1=sum(dir_num)
        print('dir_num0_1',dir_num0_1)

        print('\n\n\n',u'合计，在%s及其子文件夹中，包含字符串%s的dir文件夹个数为%s个。'%(path,str,dir_num0))

    def file_001(self):
        path=self.path
        str1=self.str1
        print('\n\n\nfile=========全路径                                        Filename')
        file_num=[]
        for root,dirs,files in os.walk(path):
            #找到文件中含有特定字符串的files的name，和根root路径进行拼接，形成绝对路径
            file_L1=[os.path.join(root, name) for name in files if name.find(str1) >=0]
            if len(file_L1)>0:
                print('\n【【【此路径下，文件个数为：',len(file_L1),'\n')
                file_num.append(len(file_L1))
                for j in file_L1:
                    abspath2 = j
                    print(abspath2,'='*10,os.path.split(abspath2)[1])

        file_num0=reduce(self.add_01,file_num)
        file_num0_1=sum(file_num)
        print('file_num0_1',file_num0_1)
        print('\n',u'合计，在%s及其子文件夹中，包含字符串%s的file文件个数为%s个。'%(path,str,file_num0))

if __name__ == '__main__':
    '''选择并输入主路径'''
    path = 'E:\\atom'

    '''输入要查询的字符串'''
    str1='py'
    s=find_file(path,str1)
    s.dir_001()
    s.file_001()
