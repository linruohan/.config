import json
import urllib.parse
import urllib.request

import easygui as g

# os.environ['TCL_LIBRARY'] = "C:\\Python36\\tcl\\tcl8.6"
# os.environ['TK_LIBRARY'] = "C:\\Python36\\tcl\\tk8.6"

if g.ccbox('是否进入翻译系统?', '小猿翻译', choices=('是', '否')):
    str1 = g.enterbox(msg="请输入翻译内容", title="xiaoyuanfanyi", default="")
else:
    g.msgbox('您已经退出。')

count = 1

while True:
    if count == 1:
        count += 1
    else:
        str1 = g.enterbox(msg="请输入翻译内容", title="xiaoyuanfanyi", default="")

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    date = {
        'type': 'AUTO',
        'i': str1,
        'doctype': 'json',
        'xmlversion': '1.8',
        'keyfrom': 'fanyi.web',
        'ue': 'utf-8',
        'action': 'FY_BY_CLICKBUTTON',
        'typeResult': 'True',
    }

    date = urllib.parse.urlencode(date).encode('utf-8')
    response = urllib.request.urlopen(url, date)
    html = response.read().decode('utf-8')
    html = json.loads(html)
    str1 = '翻译为: ' + html['translateResult'][0][0]['tgt']
    if g.ccbox(str1, choices=['继续', '退出']):
        pass
    else:
        break
