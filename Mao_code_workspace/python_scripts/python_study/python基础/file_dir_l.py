import os
from datetime import datetime
'''
dir -l显示当前目录详细信息
'''
print('Name       Size    Owner id  Group id     Modes       Last Modified  ')
print('=======================================================================')
for i in os.listdir():

    size = os.path.getsize(i)
    owner = os.stat(i).st_uid
    group = os.stat(i).st_gid
    mode = os.path.stat.filemode(os.stat(i).st_mode)
    lastmodify = datetime.fromtimestamp(os.stat(i).st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    name = i
    print('%6s   %5d %8s %10s   %12s  %4s'%(name,size,owner,group,mode,lastmodify,))
