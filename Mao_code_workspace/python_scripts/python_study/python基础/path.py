#coding=utf-8
import os,sys

# print(os.path.abspath('.'))
# print(__file__)
# s=__file__.split('\\')[-1]
# print(s)


print ("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))
print ("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])
print ("sys.path[0]=%s" % sys.path[0])

print('**'*50)
print ("os.path.abspath(__file__)=%s" % os.path.abspath(__file__))
print ("os.getcwd()=%s" % os.getcwd())
print ("sys.argv[0]=%s" % sys.argv[0])
print ("__file__=%s" % __file__)
print ("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))


# python获取当前文件路径以及父文件路径
# #当前文件的路径
# pwd = os.getcwd()
# print(pwd)
# #当前文件的父路径
# father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
# print(father_path)
# #当前文件的前两级目录
# grader_father=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
# print(grader_father)

# 获取当前文件的路径：

d = os.path.dirname(__file__)  #返回当前文件所在的目录
# __file__ 为当前文件, 若果在ide中运行此行会报错,可改为  #d = path.dirname('.')

# 获得某个路径的父级目录：
# [python] view plain copy
parent_path = os.path.dirname(d) #获得d所在的目录,即d的父级目录
parent_path  = os.path.dirname(parent_path) ##获得parent_path所在的目录即parent_path的父级目录

# 获得规范的绝对路径：

# [python] view plain copy
abspath = os.path.abspath(d) #返回d所在目录规范的绝对路径

print('current_path%s',os.path.dirname(__file__))
print ("parent_path=%s" % (os.path.dirname(os.path.dirname(__file__))))
print ("grader_father=%s" % os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
