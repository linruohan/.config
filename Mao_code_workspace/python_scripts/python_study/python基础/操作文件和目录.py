import os
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
print(os.name)
# os.uname()
# print(os.environ)
# print(os.environ.get('PATH'))

s=os.path.abspath('.')
print('当前目录的绝对路径:',s)


# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:


# 然后创建一个目录:
# os.mkdir(os.path.join(s,'/dir'))
path='\\Python\\python_lianxi\\lianxi\\dir'
print(os.path.join(os.getcwd(),path))

# os.mkdir()
print('moren',os.getcwd())
print(os.listdir())
listdir=[x for x in os.listdir('.') if os.path.isdir(x)]
print(listdir)
# # 删掉一个目录:
# os.rmdir(os.path.join(s,'/dir'))
