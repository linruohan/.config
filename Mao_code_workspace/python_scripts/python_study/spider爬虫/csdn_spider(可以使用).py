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
socket.setdefaulttimeout(5000)#设置全局超时函数
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#gb18030

headers1={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
headers2={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
headers3={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

#得到CSDN博客某一个分页的所有文章的链接
articles=set()
def getArticleLinks(pageUrl):
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
    global articles
    #return bsObj.findAll("a",href=re.compile("^/([A-Za-z0-9]+)(/article)(/details)(/[0-9]+)*$"))
    #return bsObj.findAll("a")
    #for articlelist in bsObj.findAll("span",{"class":"link_title"}):
    for articlelist in bsObj.findAll("span",{"class":"link_title"}):#正则表达式匹配每一篇文章链接
        #print(articlelist)
        if 'href' in articlelist.a.attrs:
            if articlelist.a.attrs["href"] not in articles:
                #遇到了新界面
                newArticle=articlelist.a.attrs["href"]
                #print(newArticle)
                articles.add(newArticle)
#articlelinks=getArticleLinks("http://blog.csdn.net/hw140701")
#for list in articlelinks:
    #print(list.attrs["href"])
    #print(list.a.attrs["href"])

#写入文本
def data_out(data):
   with open("CSDN.html","a+",encoding='utf-8') as out:
       out.write('\n')
       out.write(data,)


#得到CSDN博客每一篇文章的文字内容
def getArticleText(articleUrl):
    #设置代理IP
    #代理IP可以上http://ip.zdaye.com/获取
    proxy_handler=urllib.request.ProxyHandler({'https':'111.76.129.200:808'})
    proxy_auth_handler=urllib.request.ProxyBasicAuthHandler()
    opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
    urllib.request.install_opener(opener)
    #获取网页信息
    req=request.Request(articleUrl,headers=headers1 or headers2 or headers3)
    html=urlopen(req)
    bsObj=BeautifulSoup(html.read(),"html.parser")
    #获取文章的文字内容
    for textlist in bsObj.findAll("span",style=re.compile("font-size:([0-9]+)px")):
        #正则表达式匹配文字内容标签
        data_out(textlist.get_text())
#得到CSDN博客某个博客主页上所有分页的链接，根据分页链接得到每一篇文章的链接并爬取博客每篇文章的文字
pages=set()
def getPageLinks(bokezhuye):
    #设置代理IP
    #代理IP可以上http://ip.zdaye.com/获取
     proxy_handler=urllib.request.ProxyHandler({'post':'121.22.252.85:8000'})
     proxy_auth_handler=urllib.request.ProxyBasicAuthHandler()
     opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
     urllib.request.install_opener(opener)
    #获取网页信息
     req=request.Request(bokezhuye,headers=headers1 or headers2 or headers3)
     html=urlopen(req)
     bsObj=BeautifulSoup(html.read(),"html.parser")
     #获取当前页面(第一页)的所有文章的链接
     getArticleLinks(bokezhuye)
     #去除重复的链接
     global pages
     for pagelist in bsObj.findAll("a",href=re.compile("^/([A-Za-z0-9]+)(/article)(/list)(/[0-9]+)*$")):#正则表达式匹配分页的链接
         if 'href' in pagelist.attrs:
             if pagelist.attrs["href"] not in pages:
                 #遇到了新的界面
                 newPage=pagelist.attrs["href"]
                 #print(newPage)
                 pages.add(newPage)
                 #获取接下来的每一个页面上的每一篇文章的链接
                 newPageLink="http://blog.csdn.net/"+newPage
                 getArticleLinks(newPageLink)
                 #爬取每一篇文章的文字内容
                 for articlelist in articles:
                     newarticlelist="http://blog.csdn.net/"+articlelist
                     with open('newarticlelist.html','a') as f:
                         f.write(newarticlelist)
                         f.write('\n')
                     getArticleText(newarticlelist)
#getArticleLinks("http://blog.csdn.net/hw140701")
# getPageLinks("http://blog.csdn.net/hw140701")#HW140701的博客
getPageLinks("http://blog.csdn.net/Anniejunyan/article/category/1766345")#Annie的专栏

getArticleText("http://blog.csdn.net/hw140701/article/details/55104018")
