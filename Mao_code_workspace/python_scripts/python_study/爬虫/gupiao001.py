#coding=utf-8
import requests
from bs4 import BeautifulSoup
import traceback
import re,sys,io,os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def getHTMLText(url,code='utf-8'):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=code
        return r.text
    except Exception as e:
        return ""

def getStockList(lst,stockURL):
    html=getHTMLText(stockURL,'gbk')
    soup=BeautifulSoup(html,"html.parser")
    a=soup.find_all('a')
    # print (a)
    for i in a:
        try:
            href=i.attrs['href']
            s=re.findall(r's[hz]\d{6}',href)[0]
            # print(s)
            lst.append(s)
            # print(lst)
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url=stockURL+str(stock)+".html"
        html=getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict={}
            soup=BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})#股票信息
            # print(str(stockInfo))
            name=stockInfo.find_all(attrs={'class':'bets-name'})[0]#股票名称
            print(str(name))
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList=stockInfo.find_all('dt')
            valueList=stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key=keyList[i].text
                value=valueList[i].text
                infoDict[key]=value
            count=0
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                count=count+1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst)),end='')
        except:
            traceback.print_exc()
            continue
            print('\r当前进度：{:.2f}%'.format(count*100/len(lst)),end='')
stock_list_url="http://quote.eastmoney.com/stocklist.html"
slist=[]
getStockList(slist,stock_list_url)
# print(slist)
stock_info_url='https://gupiao.baidu.com/stock/'
output_file=os.path.dirname(__file__)+'/gupiao.txt'
getStockInfo(slist,stock_info_url,output_file)
