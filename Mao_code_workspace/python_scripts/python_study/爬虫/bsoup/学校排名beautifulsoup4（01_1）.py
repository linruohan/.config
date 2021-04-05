#coding=utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import importlib,sys
importlib.reload(sys)
import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except :
        return "failed!"

def fillUnivlist(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#判断tr类型是否正确
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
            # print(tds[2].string)
def printUnivlist(ulist,num):
    tplt="{0:^2}\t{1:{3}^10}\t{2:^10}"
    print (tplt.format("排名","学校","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print (tplt.format(u[0],u[1],u[2],chr(12288)))
def main():
    uinfo=[]
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"#2016年正常，2017年u【0】为none，报错
    html=getHTMLText(url)
    fillUnivlist(uinfo,html)
    printUnivlist(uinfo,20)#20 univs

main()
