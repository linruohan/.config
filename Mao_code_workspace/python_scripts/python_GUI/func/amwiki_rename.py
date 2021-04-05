# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import os
import re


class FileRename:
    def __init__(self, path, flag="rename"):
        self.path = path
        self.flag = flag
        self.num = 0
        if flag == "rename":
            self.rename(path)
        else:
            self.rename_back(path)

    def rename(self, path):
        num = 0
        for file in os.listdir(path):
            if file in "home-首页.md$navigation.md" or path.split('.')[-1].lower() in ['jpg','png']:
                print(f"file={file}==============================skip")
                continue
            oldName = os.path.join(path, file)
            if os.path.isdir(oldName):
                self.rename(oldName)
            if not re.match(r"^\d+\-", file):
                newName = os.path.join(path, str(num) + '-' + file)
                os.rename(oldName, newName)
                print("rename :%s --> %s" % (file, str(num) + '-' + file))
                num += 1

    def rename_back(self, path):
        num = 0
        for file in os.listdir(path):
            if file in "home-首页.md$navigation.md":
                print(f"file={file}==============================skip")
                continue
            oldName = os.path.join(path, file)
            if os.path.isdir(oldName):
                self.rename_back(oldName)
            if re.match(r"^\d+\-", file):
                newName = os.path.join(path, ''.join(file.split('-')[1:]))
                os.rename(oldName, newName)
                print("renameback :%s --> %s" % (file, file.split('-')[1:]))
                num += 1


if __name__ == '__main__':
    path = r"D:\Typora_book\library"
    flag = "rename"
    FileRename(path, flag)
    print(f" {flag} done!\n")
