#coding=utf-8
import os
import requests
import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url="http://m.ip138.com/ip.asp?ip="
r=requests.get(url+'202.204.80.112')
r.encoding=r.apparent_encoding
print (r)
print(r.status_code)
print(r.text[-500:])
