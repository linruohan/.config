# -*- coding:utf-8 -*-
try:
    import configparser
except:
    from six.moves import configparser
import os,os.path
from itmsv1_mvc.common.mylog import Log as log
log=log()
class ConfigReader:
    def __init__(self,path):
        self.path=path
        self.cf = configparser.ConfigParser ()
        self.read()
    def read(self):
        # 读配置文件（ini、conf）返回结果是列表
        f=self.cf.read (self.path)
        # print(f)#['001.ini']
    def get_section(self):
        # 获取读到的所有sections (域)，返回列表类型
        sessions=self.cf.sections()
        # print(sessions)#['baseconf', 'test']
        return sessions
    def get_keys(self,key):
        # 某个域下的所有key，返回列表类型
        # test=self.cf.options ('test')
        test=self.cf.options (key)
        print(test)#['ip', 'int', 'float', 'bool']
    
    def get_items(self,key):
        # 某个域下的所有key，value对
        # test1=self.cf.items ('test')
        keys=self.cf.items (key)
        print(keys)#[('ip', '127.0.0.1'), ('int', '1'), ('float', '1.5'), ('bool', 'True')]
        return keys
    def get_value(self,opotion,key):
        # 获取某个yu下的key对应的value值
        # value = self.cf.get ('test', 'ip')
        value = self.cf.get (opotion, key)
        print(value)#127.0.0.1
        return value
    '''   1）getint (section, option)
        获取section中option的值，返回int类型数据，所以该函数只能读取int类型的值。
        （2）getboolean (section, option)
        获取section中option的值，返回布尔类型数据，所以该函数只能读取boolean类型的值。
        （3）getfloat (section, option)
        获取section中option的值，返回浮点类型数据，所以该函数只能读取浮点类型的值。
        （4）has_option (section, option)
        检测指定section下是否存在指定的option，如果存在返回True，否则返回False。
        （5）has_section (section)
        检测配置文件中是否存在指定的section，如果存在返回True，否则返回False。'''
    def add_yu_key_value(self,yu,key,value):
        # self.cf = configparser.ConfigParser ()
        # 添加一个域
        sections=self.get_section()
        n=[i for i in sections if yu == i]
        if len(n)==1:   # 域下添加一个key
            print('已存在yu值，继续添加中：')
            self.cf.set (yu, key, value)
        else:
            self.cf.add_section (yu)
            # 域下添加一个key
            self.cf.set (yu, key, value)
        # value对
        self.save()
    def save(self):
        self.cf.write (open (self.path, 'w'))
if __name__ == '__main__':

    path='001.ini'
    cs=ConfigReader(path)
    # print(cs.get_section())
    cs.add_yu_key_value ( 'yu1', 'key', 'value')
    cs.get_items('yu1')