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
    def __init__(self,path):
        self.path = path
        self.save_file()
    def chinese_contain(self,str1):
        for i in str1:
            if u'\u4e00' <= i <= u'\u9fff':
                return True
        return False
    def has_attr(self, dic1, str):
        list = [k for k, v in dic1.items() if str in k]
        if len(list): return True
        return False
    def save_file(self):
        with open(self.path, 'r', encoding='utf-8')as f:
            doc = f.read()
        data = {}
        html = doc.replace (u'\xa9', u'').encode ('utf-8', 'ignore')
        html = doc.replace (u'\xa0', u'').encode ('utf-8', 'ignore')
        page = etree.HTML (html)
        htree = etree.ElementTree (page)
        print('*'*100)
        n=0
        # # 依次打印出hdoc每个元素的文本内容和xpath路径
        for t in page.iter():
            attr=t.attrib
            text=t.text
            xpath=htree.getpath(t)
            dic = dict (attr)
            # print(dic.keys())
            print(t.tag.__str__())
            key = [k for k, v in dic.items () if self.chinese_contain (v)]

            if text and self.chinese_contain (text[:10]):
                discription = text[:10]
            elif len (key):
                discription = dic[key[0]]
            elif self.has_attr (dic, 'name'):
                discription = dic['name']
            elif self.has_attr (dic, 'value'):
                discription = dic['value']
            # elif self.has_attr(dic, 'id'):
            #     discription = dic['id']
            elif self.has_attr (dic, 'class'):
                discription = dic['class']
            else:
                discription = ''
            data[n] = {'discription': discription, 'key': key, 'attr': dict (attr), 'xpath': xpath, 'text': text}
            n += 1
        m = 0
        for k, v in data.items ():
            if v['discription']:
                m += 1
                name = (v['discription']).strip ()
                xpath = v['xpath'].strip ()
                element = 'xpath=>%s' % xpath.strip ()
                # print(name, xpath, element)
                data = str (m) +': '+ name+ ':\n' +element + '\n'
                newfile = self.path.split ('.')[0] + '.txt'
                with open (newfile, 'a', encoding='utf-8') as f:
                    f.write (data)
        print ('成功将element写入%s文件！' % newfile)


if __name__ == '__main__':
    FindXpath('卡口设备状态.html')
