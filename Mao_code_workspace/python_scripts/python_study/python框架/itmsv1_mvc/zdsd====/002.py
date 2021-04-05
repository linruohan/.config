#coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import re,time,urllib,sys,io
import requests
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
url='https://wenku.baidu.com/view/4b77344e172ded630a1cb653.html?pn=50'
page = urllib.request.urlopen(url)
html = page.read().decode('gbk').encode('utf-8').decode('utf-8')
print (html)

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html=page.read()
    return html
