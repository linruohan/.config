# -*- coding: utf-8 -*-
#
# fpath = r'C:\Windows\system.ini'
#
# with open(fpath, 'r') as f:
#     s = f.read()
#     print(s)
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# 运行代码观察结果
from io import BytesIO
from io import StringIO

b=BytesIO()
print('写前位置————',b.tell())
b.write('xiaohan'.encode('utf-8'))
print('写后位置1————',b.tell())
print('写后位置1读————',b.read())
print('写后位置置于0————',b.seek(0))
print('获取位置2————',b.tell())
print('写后位置置于0读取1————',b.read())
b.write(b'123')
print('获取位置2——3——',b.tell())
print('读取2————',b.read())
print('读取2————',b.readlines())
print('获取值————',b.getvalue())


s=StringIO('hello,world')
print(s.getvalue())
