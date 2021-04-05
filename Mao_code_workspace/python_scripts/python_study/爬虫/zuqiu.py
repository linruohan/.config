#coding=utf-8

import importlib,sys
importlib.reload(sys)

import requests
from bs4 import BeautifulSoup
import bs4
import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string])
def printUnivList(ulist, num):
    print("排名","球队")
    for i in range(num):
        u=ulist
        if(i>1):
            print(u[0],u[1])

def main():
    uinfo = []
    url = 'https://nba.hupu.com/stats/teams'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

main()
