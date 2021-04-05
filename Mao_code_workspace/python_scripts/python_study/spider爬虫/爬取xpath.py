import urllib,urllib.request
import lxml
import lxml.html as HTML
import lxml.etree as etree

#设置url参数
lin = 'en'
lout = 'zh-CN'
text = 'my apple 123'
values = {'hl':'zh-CN', 'ie':'UTF-8', 'text':text, 'sl':lin, 'tl':lout}
url = 'http://www.baidu.com'
data = urllib.parse.urlencode(values).encode('utf-8 ')
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# req = urllib.request.Request(url, data=data, headers=headers)
# response = urllib.request.urlopen(req)
#
#
headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
data1 = urllib.request.Request(url, headers=headers)
data = urllib.request.urlopen(data1).read()
print(urllib.request.urlopen(url).getcode())
# shtml = urllib.request.urlopen(req).read()
# response.close()

# hdoc = HTML.fromstring(shtml)
print(hdoc)
htree = etree.ElementTree(hdoc)

#依次打印出hdoc每个元素的文本内容和xpath路径
# for t in hdoc.iter():
#     print (htree.getpath(t))
#     print (t.text_content())
#     raw_input()
