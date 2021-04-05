# -*- coding: cp936 -*-
import os
class Filenames:

    def all_path(self, path):
        result = []
        for maindir, subdir, file_name_list in os.walk(path):
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)
                result.append(apath)
        # print(result)
        print('共有%s个文件,进行预处理。' % len(result))
        return result

    def names(self, paths, pattern, type):
        names = []
        for i in paths:
            n = 1
            if i.split('.')[-1] != pattern:
                name = i.split(type)[0]
                if name in names:
                    name += str(n)
                singlename = name.split('\\')[-1]
                names.append(singlename)
        print('总共得到%s个文件名'%len(names))
        return names

    def rename(self, result, pattern, type):
        names = []
        for i in result:
            n = 1
            if not i.split('.')[-1] == pattern:
                name = i.split(type)[0]
                if name in names:
                    name += str(n)
                names.append(name)
                print(name)
                os.rename(i, name + type)
            n += 1


if __name__ == '__main__':
    # 过滤的文件格式
    pattern = 'onetoc2'
    # 搜索文件格式
    type = '.one'
    path ='F:\\onenote笔记本\\20180321笔记本\\jintao 的笔记本'
    s = Filenames()
    paths=s.all_path(path)
    names=s.names(paths, pattern, type)
    print(names)