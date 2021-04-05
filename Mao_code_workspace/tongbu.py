#  -*- coding: utf-8 -*-
from bypy import ByPy
import os
import shutil


class BypyBackup:
    def __init__(self, paths):
        self.bp = ByPy()
        self.paths = paths
        self.do_update()

    def do_update(self, zip=True):
        for path in self.paths:
            pstr = path.split("\\")[-1]
            remote_path = pstr + "/" + pstr + ".zip"
            print(path+"\t"+remote_path)
            if zip:    
                self.zip_tongbu(path, remote_path)
            else:
                self.no_zip_tongbu(path, remote_path)

    def no_zip_tongbu(self, path, remote_path):
        print("同步 [%s] 文件......" % path)
        if self.bp.list(path):
            # 云端不存在  upload
            # print("bu cunzai")
            self.bp.upload(localpath=path,
                           remotepath=remote_path,
                           ondup='overwrite')
        else:
            # 云端存在 syncup
            # print("cunzai")
            self.bp.syncup(localdir=(path + ".zip"), remotedir=remote_path)

    def zip_tongbu(self, path, remote_path):
        # 压缩
        if shutil.make_archive(path, "zip", path):
            print("同步 [%s] zip文件......" % path)
            if self.bp.list(remote_path):
                # 云端不存在  upload
                # print("bu cunzai")
                self.bp.upload(localpath=(path + ".zip"),
                               remotepath=remote_path,
                               ondup='overwrite')
            else:
                # 云端存在 syncup
                # print("cunzai")
                self.bp.syncup(localdir=(path + ".zip"), remotedir=remote_path)
        os.remove(path + ".zip")

    def download(self, path):
        # 下载单个文件
        self.bp.download(remotepath=u'hello/bypy_help.txt',
                         localpath=u'help_yun.txt')

        # 比较本地当前目录和云盘（程序的）根目录（这个很有用）但是我还是不会用
        self.bp.compare(remotedir='hello/',
                        localdir=u'',
                        skip_remote_only_dirs=False)
        # 将云盘同步到本地
        self.bp.syncdown(remotedir=u'hello/',
                         localdir=u'elang_demo/',
                         deletelocal=False)
        # 添加离线下载(我这里用不了)
        source_url = 'magnet:?xt=urn:btih:AADDA6A3D1E3BA768AF7BCD188C35A44F9D33357&dn=\
            %5B%E5%93%86%E5%95%A6A%E6%A2%A6%E5%89%A7%E5%9C%BA%E7%89%88%5D%5BDoraemon\
            %20Movie%5D%5B1980-2016%5D%5B01-37%5D%5B%E5%9B%BD%E7%B2%A4%E6%97%A53%E9%9F\
            %B3%E8%BD%A8%5D%5B%E7%AE%80%E7%B9%81%E5%AD%97%E5%B9%95%5D'

        self.bp.cdl_add(source_url, save_path=u'hello/多拉a梦剧场版/', timeout=3600)


if __name__ == "__main__":
    paths = [
        r"C:\Users\Administrator\Desktop",  # 桌面
        r"D:\workspace",  # 代码工作区
        r"D:\娱乐\读书ireader",  # 小说阅读
        r"D:\娱乐\lofter",  # lofter图片
        r"D:\图片",  # window下载图片
        #r"D:\学习linux C  shell",  # 学习PDF资料
        r"D:\下载",  # 收藏软件安装包
        r"D:\娱乐\Music",  # 音乐
    ]
    b = BypyBackup(paths)
    print("Successfully  !!!!")