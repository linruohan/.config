#coding=utf-8

import json
import urllib
import requests
import re
import lxml
from lxml import etree
'''花瓣网
'''
url='https://huaban.com'
page = requests.get(url)
html = page.content
re=r'<div class="title">(.?*)</div>'
name=html.split('<div class="title">')
print html

# print h1
'''
response = requests.get(url)
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
# reg = r'src="(.*?)"'
# imgre = re.compile(reg)
# imglist = re.findall(imgre,html)
# x = 0
# for imgurl in imglist:
#     urllib.urlretrieve(imgurl,'%s.jpg' % x)
#     x+=1
'''
'''知乎网站'''
header = {

    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response =requests.get(url,headers=header)
html1=response.text
# print(html1)
