#coding=utf-8
import io
import os
import sys
import urllib
from urllib.request import  urlopen
from urllib  import request
from bs4 import BeautifulSoup
import datetime
import random
import re
import requests
import socket
socket.setdefaulttimeout(5000)

'''=======================输入csdn博客网站地址：=================================='''
url='http://blog.csdn.net/hw140701'
'''========================================================='''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')#gb18030

articles=set()

headers1={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
headers2={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
headers3={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}


#设置代理IP
#代理IP可以上http://ip.zdaye.com/获取
proxy_handler=urllib.request.ProxyHandler({'post':'210.136.17.78:8080'})
proxy_auth_handler=urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
urllib.request.install_opener(opener)
#获取网页信息
req=request.Request(pageUrl,headers=headers1 or headers2 or headers3)
html=urlopen(req)
bsObj=BeautifulSoup(html.read(),"html.parser")
urllist=[]
titlelist=[]
s0=bsObj.findAll("span",{"class":"link_title"})
for si in s0:
    href=si.a.attrs["href"]
    s1=si.get_text()
    titlelist.append(s1)
    h1="http://blog.csdn.net/"+str(href)
    urllist.append(h1)
# for i in




# print(bsObj)
global articles
#return bsObj.findAll("a",href=re.compile("^/([A-Za-z0-9]+)(/article)(/details)(/[0-9]+)*$"))
for articlelist in bsObj.findAll("span",{"class":"link_title"}):#正则表达式匹配每一篇文章链接

    if 'href' in articlelist.a.attrs:
        if articlelist.a.attrs["href"] not in articles:
            #遇到了新界面
            newArticle=articlelist.a.attrs["href"]
            #print(newArticle)
            articles.add(newArticle)
# print(articles)
    # print(articlelist.get_text())

# return bsObj

def data_out(data):
   with open("卡口设备状态.html","a+",encoding='utf-8') as out:
       out.write('\n')
       out.write(data,)
# print(articles)

# data_out(s)
