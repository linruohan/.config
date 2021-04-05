#coding=utf-8
import requests
import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("")
def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])#eval去掉双引号
            ilt.append([price,title])
    except:
        print("")
def printGoodslist(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
def main():
    goods='书包'#关键字
    depth=4#爬取几页
    start_url='https://s.taobao.com/search?q='+goods
    infolist=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infolist,html)
        except :
            continue
    printGoodslist(infolist)

main()
