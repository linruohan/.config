#coding=utf-8
import requests
import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url="http://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[0:2000])
except:
    print("爬取失败！")
