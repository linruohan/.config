#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import shutil
import sys
import logging

'''注：

1，日志会输出到SynDirTool.py文件的相同目录的SynDirTool.log文件中
2，如果目的文件夹已有该文件，且该文件较新，则不再会复制源文件夹中的文件'''


class SynDirTool:
    def __init__(self, fromdir, todir):
        self.fromdir = fromdir
        self.todir = todir

    def synDir(self):
        return self.__copyDir(self.fromdir, self.todir)

    def __copyDir(self, fromdir, todir):
        # 防止该目录不存在，创建目录
        self.__mkdir(todir)
        count = 0
        for filename in os.listdir(fromdir):
            if filename.startswith('.'):
                continue
            fromfile = fromdir + os.sep + filename
            tofile = todir + os.sep + filename
            if os.path.isdir(fromfile):
                count += self.__copyDir(fromfile, tofile)
            else:
                count += self.__copyFile(fromfile, tofile)
        return count

    def __copyFile(self, fromfile, tofile):
        if not os.path.exists(tofile):
            shutil.copy2(fromfile, tofile)
            logging.info("新增%s ==> %s" % (fromfile, tofile))
            return 1
        fromstat = os.stat(fromfile)
        tostat = os.stat(tofile)
        if fromstat.st_ctime > tostat.st_ctime:
            shutil.copy2(fromfile, tofile)
            logging.info("更新%s ==> %s" % (fromfile, tofile))
            return 1
        return 0

    def __mkdir(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号 或者 /
        path = path.rstrip(os.sep)

        # 判断路径是否存在
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            logging.info(path + ' 目录创建成功')


if __name__ == '__main__':
    count = 0
    srcdir = sys.argv[1]
    descdir = sys.argv[2]
    logging.basicConfig(filename='SynDirTool.log', level=logging.INFO)
    tool = SynDirTool(srcdir, descdir)
    count += tool.synDir()
