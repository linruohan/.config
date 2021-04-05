#encoding=utf-8
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os,sys,io
from lxml import etree
import lxml.html as HTML
from urllib.request import urlopen
from urllib import request
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class FindXpath(object):
    """docstring for FindXpath."""
    def __init__(self, driver,url):
        self.url = url
        self.driver = driver#用的谷歌，到http://chromedriver.storage.googleapis.com/index.htm 下载
        self.html=None
        self.title=''
    def getHtml(self):
        driver=self.driver
        driver.maximize_window()
        driver.set_page_load_timeout(10)
        driver.get(self.url)
        self.title=driver.title
        self.html=driver.page_source.encode('GBK', 'ignore')
        return self.html

    def att_text(self):
        element_dict=[]
        html=str(self.getHtml())
        page = etree.HTML(html)
        htree = etree.ElementTree(page)
        # 依次打印出hdoc每个元素的文本内容和xpath路径
        title=str(self.title)
        for t in page.iter():
            # print (htree.getpath(t))
            # print (t.attrib)
            # print(t.text)
            element_dict.append(t)
        return element_dict

if __name__ == '__main__':
    url='http://193.169.100.249:8086/itmsld/login'
    driver=webdriver.Chrome()
    f=FindXpath(driver,url)
    element_dict=f.att_text()
    print(element_dict)
