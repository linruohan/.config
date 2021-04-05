import io
import sys
import os

# 获取当前文件的路径：
from os import path
d = path.dirname(__file__)  # 返回当前文件所在的目录
# __file__ 为当前文件, 若果在ide中运行此行会报错,可改为 #d = path.dirname('.')

# 获得某个路径的父级目录：
parent_path = os.path.dirname(d)  # 获得d所在的目录,即d的父级目录
# 获得parent_path所在的目录即parent_path的父级目录
parent_path = os.path.dirname(parent_path)

# 获得规范的绝对路径：
abspath = path.abspath(d)  # 返回d所在目录规范的绝对路径

'''获得当前路径
'''
cwd = os.getcwd()
print(d)
# 获取当前文件的路径：
d = path.dirname(__file__)  # 返回当前文件所在的目录
# __file__ 为当前文件, 若果在ide中运行此行会报错,可改为 #d = path.dirname('.')

# 获得某个路径的父级目录：
parent_path = os.path.dirname(d)  # 获得d所在的目录,即d的父级目录
# 获得parent_path所在的目录即parent_path的父级目录
gradparent_path = os.path.dirname(parent_path)

# 获得规范的绝对路径：
abspath = path.abspath(d)  # 返回d所在目录规范的绝对路径
print(d)
print(parent_path)
print(gradparent_path)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d = os.path.dirname(__file__)
os.chdir(d)
sys.path.append((d, os.path.dirname(d)))
'''
  得到当前文件夹下的所有文件和文件夹
'''
print(os.listdir())


'''
 delete file
'''
# os.remove('sw724.vaps')
# print(os.listdir())


'''
 删除单个目录和多个目录
#  '''
# os.removedir()
# os.removedir()


'''
 检查是否是文件／文件夹
'''
# print(os.path.isfile('/Users/liuxiaolong/PycharmProjects/untitled/sw724.vaps'))
# print(os.path.isdir('/Users/liuxiaolong/PycharmProjects/untitled/sw724.vaps'))


'''
 检查文件路径是否存在
'''

# print(os.path.exists('/Users/liuxiaolong/PycharmProjects/untitled/iiii'))

'''
 分离文件名
 分离扩展名

'''
# [dirname,filename]=os.path.split('/Users/liuxiaolong/PycharmProjects/untitled/sw724.vaps')
# print(dirname,"\n",filename)

# [fname,fename]=os.path.splitext('/Users/liuxiaolong/PycharmProjects/untitled/sw724.vaps')
# print(fname,"\n",fename)

'''
 获得文件路径
 获得文件名
 获得当前环境
'''
# print("get pathname:",os.path.dirname('/Users/liuxiaolong/PycharmProjects/untitled/sw724.vaps'))
# print("get filename:",os.path.basename('/Users/liuxiaolong/PycharmProjects/untitled/sw724.vaps'))
# print(os.getenv)
