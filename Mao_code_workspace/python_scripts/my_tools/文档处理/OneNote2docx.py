# -*- coding: cp936 -*-
import os
path = 'E:\onenote\16.0\新建文件夹\\'
# for root,dir,files in os.walk(path):
#     # print(root)
#     for root1,dir1,files1 in os.walk(root):
#         print(root1)
def all_path(path):
    result = []
    for maindir, subdir, file_name_list in os.walk(path):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    # print(result)
    # print(len(result))
    return result
names=[]
for i in all_path(path):
    n = 1
    print(i)
    if not i.split('.')[-1]=='onetoc2':
        name=i.split('.one')[0]
        if name in names:
            name+=str(n)
        names.append(name)
        print( name)
        os.rename(i, name + ".docx")
    n+=1