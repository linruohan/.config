#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import re
path='卡口设备状态.html'
with open (path, 'r', encoding='utf-8')as f:
    doc = f.read ()
data = {}
html = doc.replace (u'\xa9', u'').encode ('utf-8', 'ignore')
html = doc.replace (u'\xa0', u'').encode ('utf-8', 'ignore')
soup = BeautifulSoup(html,'html.parser', from_encoding='utf-8')
# print (soup.prettify()  )


input=soup.find_all ('input')
button=soup.find_all('button')
# print(s)
for i in button:
    print(i.attrs)
# print (soup.find_all ())
# print (soup.a.attrs)
