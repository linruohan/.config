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

def chinese_contain(str1):
    for i in str1:
        if u'\u4e00'<=i<=u'\u9fff':
            return True
    return False

class FindXpath(object):
    """docstring for FindXpath."""
    def __init__(self,html):
        self.html = html

    def save_file(self):
        attribs=[]
        contents=[]
        xpaths=[]
        driver=self.driver
        title=driver.title
        html=self.html.replace(u'\xa9', u'').encode('utf-8', 'ignore')
        page = etree.HTML(html)
        # ids = page.xpath(u"//*[@id='menu_130402081930284387431bd38d30c4ac']/p/a")
        # for x in ids:
        #     print (x.attrib)
            # print(x.text)
        print('*'*100)
        htree = etree.ElementTree(page)
        # # 依次打印出hdoc每个元素的文本内容和xpath路径
        for t in page.iter():
            attr=t.attrib
            text=t.text
            xpath=htree.getpath(t)
            attribs.append(t.attrib)
            contents.append(t.text)
            xpaths.append(htree.getpath(t))
            # print(t.attrib)
            with open('ld_xpath.html','a') as f:
                s=str(htree.getpath(t)+'\n\r'+str(t.text))
                f.write(s)
        print(attribs[0],contents[0],xpaths[0])
if __name__ == '__main__':
    FindXpath()