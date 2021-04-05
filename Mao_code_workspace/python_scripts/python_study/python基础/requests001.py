# coding=utf-8
import requests,urllib

r=requests.get("http://www.baidu.com")
print (r.status_code)
print (r.encoding)
print (r.apparent_encoding)
r.encoding='utf-8'
print (r.text)
