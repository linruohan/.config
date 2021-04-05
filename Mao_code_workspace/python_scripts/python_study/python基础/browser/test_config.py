# coding=utf-8
import configparser
import os


class TestReadConfigFile(object):

    def get_value(self):
        root_dir = os.path.abspath('.') # 获取项目根目录的相对路径
        print ('root_dir:'+root_dir)

        config = configparser.ConfigParser()
        file_path =os.path.abspath('.')+ '/config/config.ini'
        print('file_path:'+file_path)
        config.read(file_path)

        browser = config.get("browserType", "browserName1")
        url = config.get("testServer", "URL1")

        return(browser,url)  # 返回的是一个元组

trcf = TestReadConfigFile()
print (trcf.get_value())
